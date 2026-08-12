# frozen_string_literal: true

require "json"
require "liquid"

root = File.expand_path("..", __dir__)
contributors = JSON.parse(File.read(File.join(root, "_data", "contributors.json")))
index_source = File.read(File.join(root, "index.md"), encoding: "UTF-8")
index_body = index_source.sub(/\A---\s*\n.*?\n---\s*\n/m, "")
layout_source = File.read(File.join(root, "_layouts", "default.html"), encoding: "UTF-8")

site = {
  "title" => "VeryMath",
  "description" => "AI for mathematical research. Reusable, verifiable, and collaborative workflows for open mathematics.",
  "data" => { "contributors" => contributors }
}
page = { "title" => "VeryMath" }
assigns = { "site" => site, "page" => page }

content = Liquid::Template.parse(index_body, error_mode: :strict).render!(
  assigns,
  strict_variables: true,
  strict_filters: true
)
html = Liquid::Template.parse(layout_source, error_mode: :strict).render!(
  assigns.merge("content" => content),
  strict_variables: true,
  strict_filters: true
)

$stdout.write(html)
