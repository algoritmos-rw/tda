#!/usr/bin/env ruby
# tools/fill_descriptions.rb
# Scans markdown files under docs/ and adds a 'description' front-matter entry
# if missing, using the first paragraph (excerpt) truncated to 160 chars.

require 'yaml'
require 'fileutils'

ROOT = File.expand_path('../../docs', __dir__)

files = Dir.glob(File.join(ROOT, '**', '*.md'))
puts "Found #{files.size} markdown files"

files.each do |path|
  text = File.read(path)
  if text =~ /\A---\s*\n(.*?)\n---\s*\n/m
    fm_text = $1
    body = $'
    fm = YAML.safe_load(fm_text) || {}
    if fm['description'] && !fm['description'].to_s.strip.empty?
      # skip
      next
    end
    # find first non-empty paragraph
    excerpt = body.split(/\n\s*\n/).find { |p| p.strip.length > 0 } || ''
    excerpt = excerpt.gsub(/\[.*?\]\(.*?\)/, '') # remove links
    excerpt = excerpt.gsub(/\!\[.*?\]\(.*?\)/, '') # remove images
    excerpt = excerpt.strip.gsub(/\s+/, ' ')
    excerpt = excerpt[0,160]
    fm['description'] = excerpt
    new_fm = YAML.dump(fm).strip
    new_text = "---\n#{new_fm}\n---\n\n#{body}"
    File.write(path, new_text)
    puts "Wrote description for #{path}"
  else
    # no front matter, add minimal front matter with description
    body = text
    excerpt = body.split(/\n\s*\n/).find { |p| p.strip.length > 0 } || ''
    excerpt = excerpt.gsub(/\[.*?\]\(.*?\)/, '')
    excerpt = excerpt.gsub(/\!\[.*?\]\(.*?\)/, '')
    excerpt = excerpt.strip.gsub(/\s+/, ' ')
    excerpt = excerpt[0,160]
    fm = { 'description' => excerpt }
    new_fm = YAML.dump(fm).strip
    new_text = "---\n#{new_fm}\n---\n\n#{body}"
    File.write(path, new_text)
    puts "Added front matter + description for #{path}"
  end
end

puts "Done."
