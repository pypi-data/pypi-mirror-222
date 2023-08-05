#[macro_use]
extern crate lazy_static;
use ammonia::Builder;
use pulldown_cmark as md;
use regex::{Captures, Regex};
use std::collections::HashMap;

pub struct User {
    pub username: String,
    pub user_id: String,
    pub link: String,
    pub fullname: String,
}

lazy_static! {
    // Feels a little hacky matching angle brackets, but it's
    // to allow the tag to be immediately after a html tag
    static ref USER_REGEX: Regex = Regex::new(r"(^|\s|<[^>]*>)@(\w+|\d+)").unwrap();
}

#[derive(Default)]
pub struct Markmini {
    tag_to_link: HashMap<String, String>,
}

impl Markmini {
    pub fn new() -> Self {
        return Default::default();
    }

    pub fn add_users(&mut self, users: Vec<User>) {
        for u in users {
            let link = String::from("<a href=\"") + &u.link + "\">" + &u.fullname + "</a>";
            self.tag_to_link.insert(u.user_id, link.clone());
            self.tag_to_link.insert(u.username, link);
        }
    }

    pub fn compile(&self, input: &str) -> String {
        let mut output = self.mardownify(input);
        output = self.replace_tags_with_links(&output);
        output = self.sanitize(&output);
        return output;
    }

    fn mardownify(&self, input: &str) -> String {
        let mut options = md::Options::empty();
        // Enable some Github flavored markdown features
        options.insert(md::Options::ENABLE_STRIKETHROUGH);
        options.insert(md::Options::ENABLE_TABLES);
        options.insert(md::Options::ENABLE_TASKLISTS);
        let parser = md::Parser::new_ext(input, options);
        let mut output = String::new();
        md::html::push_html(&mut output, parser);
        return output;
    }

    fn replace_tags_with_links(&self, input: &str) -> String {
        println!("{input}");
        let replacer = |c: &Captures| match self.tag_to_link.get(&c[2]) {
            // Note: capture 0 is entire match, capture 1 is the optional leading whitespace, capture 2 is the uid or username
            Some(link) => String::new() + &c[1] + link,
            None => String::new() + &c[1] + "@" + &c[2],
        };
        let output = USER_REGEX.replace_all(input, replacer);

        return output.to_string();
    }

    /// Sanitize output html to avoid security issues
    fn sanitize(&self, input: &str) -> String {
        // Ammonia sanitizes our output html.
        // It's defaults are very strict so we whitelist som
        return Builder::default()
            // allow lit component html tags
            .add_tags(&["t-spoiler", "t-quote"])
            .clean(input)
            .to_string();
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn regular_markdown() {
        let compiler = Markmini::new();
        let result = compiler.compile("# Hello world!");
        assert_eq!(result, "<h1>Hello world!</h1>\n");

        let result = compiler.compile("Midway in writing <");
        assert_ne!(result, "");
    }

    #[test]
    fn with_users() {
        let mut compiler = Markmini::new();
        compiler.add_users(vec![User {
            user_id: "1".to_string(),
            username: "testy".to_string(),
            link: "/users/1".to_string(),
            fullname: "Test McTestern".to_string(),
        }]);

        let result = compiler.compile("Yo @testy se her");
        assert_eq!(
            result,
            "<p>Yo <a href=\"/users/1\" rel=\"noopener noreferrer\">Test McTestern</a> se her</p>\n"
        );

        let result = compiler.compile("@testy se her");
        assert_eq!(
            result,
            "<p><a href=\"/users/1\" rel=\"noopener noreferrer\">Test McTestern</a> se her</p>\n"
        );

        let result = compiler.compile("@finsikke finnes ikke");
        assert_eq!(result, "<p>@finsikke finnes ikke</p>\n");

        let result = compiler.compile("Hey, @finsikke finnes ikke");
        assert_eq!(result, "<p>Hey, @finsikke finnes ikke</p>\n");

        let result = compiler.compile("# @testy");
        assert_eq!(
            result,
            "<h1><a href=\"/users/1\" rel=\"noopener noreferrer\">Test McTestern</a></h1>\n"
        )
    }
}
