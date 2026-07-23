#!/usr/bin/env ruby

# frozen_string_literal: true

require "find"
require "pathname"
require "time"
require "yaml"

REPO_ROOT = Pathname.new(File.expand_path("../..", __dir__))
CONFIG_PATH = REPO_ROOT.join("config/source-types.yaml")
RECORD_TYPES_PATH = REPO_ROOT.join("config/record-types.yaml")
REGISTER_PATH = REPO_ROOT.join("registers/sources.yaml")

def load_yaml(path)
  YAML.safe_load(File.read(path), aliases: false)
end

def ignored?(name, patterns)
  patterns.any? { |pattern| File.fnmatch?(pattern, name, File::FNM_DOTMATCH) }
end

def custody_path(relative_path)
  mappings = [
    ["agentic_ai/research/", "AI_Agency/"],
    ["current_state/unclassified_research/", "Muscellaneous /"],
    ["engineering_platform/ai_types/", "AI_Types_Traditional_and_Generative/"],
    ["engineering_platform/prompt_and_context_engineering/", "AI_Prompt_and_Context_Engineering/"],
    ["ecosystem_sourcing/", "ecosystem_sourcing/"],
    ["glossary_vocabulary/", "AI_Gloassary_Vocabluary/"],
    ["governance/research/adaptive_governance/", "AI_Governance /Adaptive_Governance/"],
    ["governance/research/cost_and_value_governance/", "AI_Governance /cost_and_value_governance/"],
    ["governance/research/governance_policies_and_how_to/", "AI_Governance /Governance_Policies_and_Howto/"],
    ["governance/research/", "AI_Governance /"],
    ["organization/research/", "AI_Adoption_Organization/"],
    ["security_trust/risks_trust_security_management/", "AI_Risks_Trust_SecurityManagement/"],
    ["security_trust/security/", "AI_Security/"],
    ["strategic_intent/general_presentation_draft/", "AI_Adoption_General_Presentation_Draft/"],
    ["strategic_intent/vision/", "AI_Adoption_Vision /"],
    ["use_cases/general_use/", "AI_USE/"],
    ["use_cases/telecom/", "AI_Telecom/"],
    ["use_cases/catalogue/", "AI_Use_Cases /"]
  ]

  exact = {
    "data/overview.mmd" => "AI_adoption_MindMap/AI_DATA.mmd",
    "decision_environment/technology-generational-moment-generative-ai-cio-cto-guide.pdf" => "technologys-generational-moment-with-generative-ai-a-cio-and-cto-guide.pdf",
    "engineering_platform/overview.mmd" => "AI_adoption_MindMap/AI_ENGINEERING.mmd",
    "governance/overview.mmd" => "AI_adoption_MindMap/GOVERNANCE.mmd",
    "maturity_execution/models/AI-Maturity-Model-Overview.pdf" => "AI_Maturity_Models_Adoption /AI-Maturity-Model-Overview.pdf",
    "organization/overview.mmd" => "AI_adoption_MindMap/AI_ORGANIZATION.mmd",
    "people_and_culture/overview.mmd" => "AI_adoption_MindMap/AI_PEOPLE_and_CULTURE.mmd",
    "strategic_intent/strategy.mmd" => "AI_adoption_MindMap/AI_STRATEGY.mmd",
    "strategic_intent/vision.mmd" => "AI_adoption_MindMap/AI_VISION.mmd",
    "value_management/value_creation.mmd" => "AI_adoption_MindMap/AI_VALUE_CREATION.mmd"
  }

  return exact[relative_path] if exact.key?(relative_path)

  mapping = mappings.find { |current, _original| relative_path.start_with?(current) }
  return nil unless mapping

  current, original = mapping
  original + relative_path.delete_prefix(current)
end

def intermediate_paths(relative_path)
  case relative_path
  when %r{\Aglossary_vocabulary/}
    [relative_path.sub(%r{\Aglossary_vocabulary/}, "people_and_culture/glossary_vocabulary/")]
  when %r{\Ause_cases/general_use/}
    [relative_path.sub(%r{\Ause_cases/general_use/}, "value_and_use_cases/general_use/")]
  when %r{\Ause_cases/telecom/}
    [relative_path.sub(%r{\Ause_cases/telecom/}, "value_and_use_cases/telecom/")]
  when %r{\Ause_cases/catalogue/}
    [relative_path.sub(%r{\Ause_cases/catalogue/}, "value_and_use_cases/use_cases/")]
  when "value_management/value_creation.mmd"
    ["value_and_use_cases/value_creation.mmd"]
  when "maturity_execution/models/AI-Maturity-Model-Overview.pdf"
    ["maturity_execution/maturity_models/AI-Maturity-Model-Overview.pdf"]
  else
    []
  end
end

def path_history(original_path, current_path)
  history = [{
    "event_date" => "2026-07-21",
    "event_type" => "originally_observed",
    "from_relative_path" => nil,
    "to_relative_path" => original_path,
    "reason" => "Recorded from the read-only source-access verification."
  }]

  previous = original_path
  intermediate_paths(current_path).each do |intermediate|
    history << {
      "event_date" => "2026-07-21",
      "event_type" => "taxonomy_reorganization",
      "from_relative_path" => previous,
      "to_relative_path" => intermediate,
      "reason" => "User-approved physical taxonomy reorganization before the custody baseline."
    }
    previous = intermediate
  end

  if previous != current_path
    maturity_change = current_path.start_with?("maturity_execution/models/")
    history << {
      "event_date" => maturity_change ? "2026-07-22" : "2026-07-21",
      "event_type" => intermediate_paths(current_path).empty? ? "taxonomy_reorganization" : "semantic_separation",
      "from_relative_path" => previous,
      "to_relative_path" => current_path,
      "reason" => maturity_change ? "Placed under the approved maturity-model collection." : "Placed under the approved repository-aligned source taxonomy."
    }
  end

  history
end

config = load_yaml(CONFIG_PATH)
record_types_config = load_yaml(RECORD_TYPES_PATH)
source_root = Pathname.new(config.fetch("source_root").fetch("path"))
ignored_patterns = config.fetch("ignored_files")
path_rules = config.fetch("source_prefix_path_rules")
prefixes = config.fetch("source_id_prefixes")
domain_defaults = config.fetch("source_category_taxonomy_defaults")
knowledge_defaults = config.fetch("source_category_knowledge_layer_defaults", {})
collection_targets = record_types_config.fetch("source_collection_record_targets")

extension_types = config.fetch("source_types").each_with_object({}) do |(type, settings), result|
  settings.fetch("extensions").each { |extension| result[extension.downcase] = type }
end

existing_records = load_yaml(REGISTER_PATH).fetch("records", [])
existing_by_path = existing_records.to_h { |record| [record.fetch("current_relative_path"), record.fetch("source_id")] }

files = []
symlinks = []
Find.find(source_root.to_s) do |absolute_path|
  path = Pathname.new(absolute_path)
  next if path == source_root

  relative_path = path.relative_path_from(source_root).to_s
  metadata = File.lstat(absolute_path)

  if metadata.symlink?
    symlinks << relative_path
    Find.prune if metadata.directory?
    next
  end

  if ignored?(path.basename.to_s, ignored_patterns)
    Find.prune if metadata.directory?
    next
  end

  next if metadata.directory?
  next unless metadata.file?

  files << [relative_path, metadata]
end

raise "Symbolic links require manual review: #{symlinks.join(', ')}" unless symlinks.empty?

current_paths = files.map(&:first)
missing_paths = existing_by_path.keys - current_paths
raise "Catalogue paths disappeared; record a custody event first: #{missing_paths.join(', ')}" unless missing_paths.empty?

entries = files.sort_by(&:first).map do |relative_path, metadata|
  matching_rule = path_rules
    .select do |rule|
      rule_path = rule.fetch("current_relative_path")
      relative_path == rule_path || relative_path.start_with?("#{rule_path}/")
    end
    .max_by { |rule| rule.fetch("current_relative_path").length }
  raise "No source-category rule for #{relative_path}" unless matching_rule

  category = matching_rule.fetch("source_category")
  category_prefix = prefixes.fetch(category)
  existing_source_id = existing_by_path[relative_path]
  assignment_basis = if existing_source_id && !existing_source_id.start_with?("#{category_prefix}-")
                       legacy_prefix = existing_source_id.sub(/-[0-9]{6}\z/, "")
                       "legacy_source_id_preserved:#{legacy_prefix};longest_path_rule:#{matching_rule.fetch('current_relative_path')}"
                     else
                       "longest_path_rule:#{matching_rule.fetch('current_relative_path')}"
                     end
  extension = File.extname(relative_path).downcase
  original_path = custody_path(relative_path)
  raise "No custody mapping for #{relative_path}" unless original_path

  matching_target = collection_targets
    .select do |collection_path, _targets|
      relative_path == collection_path || relative_path.start_with?("#{collection_path}/")
    end
    .max_by { |collection_path, _targets| collection_path.length }
  proposed_record_types = if matching_target
                            matching_target.last.dup
                          else
                            case category
                            when "glossary" then ["glossary_term"]
                            when "use_cases", "telecom" then ["use_case_pattern"]
                            else []
                            end
                          end

  {
    "source_id" => existing_source_id,
    "source_category" => category,
    "prefix_assignment_basis" => assignment_basis,
    "source_root_id" => config.fetch("source_root").fetch("id"),
    "original_filename" => File.basename(original_path),
    "original_relative_path" => original_path,
    "current_filename" => File.basename(relative_path),
    "current_relative_path" => relative_path,
    "path_history" => path_history(original_path, relative_path),
    "domain_ids" => [],
    "proposed_domain_ids" => domain_defaults.fetch(category, []).dup,
    "knowledge_layer_ids" => knowledge_defaults.fetch(category, []).dup,
    "business_domain_ids" => [],
    "ai_technique_ids" => [],
    "proposed_record_types" => proposed_record_types,
    "source_type" => extension_types.fetch(extension, "unsupported"),
    "extension" => extension,
    "size_bytes" => metadata.size,
    "filesystem_modified_at" => metadata.mtime.utc.iso8601,
    "hash_algorithm" => nil,
    "content_hash" => nil,
    "hash_calculated_at" => nil,
    "processing_state" => "metadata_catalogued",
    "classification" => "pending",
    "classification_basis" => "metadata_only_not_reviewed",
    "classification_reviewed_by" => nil,
    "classification_reviewed_at" => nil,
    "processing_route" => "pending",
    "processing_route_approved_by" => nil,
    "processing_route_approved_at" => nil,
    "approved_external_service" => nil,
    "approved_account" => nil,
    "approved_purpose" => nil,
    "contains_personal_data" => nil,
    "contains_credentials" => nil,
    "contains_restricted_operational_data" => nil,
    "rights_or_license_status" => "pending",
    "handling_notes" => "Metadata only; document content has not been analyzed.",
    "extraction_record_ids" => [],
    "approved_tool" => nil,
    "tool_version" => nil,
    "ocr_required" => nil,
    "duplicate_status" => "unchecked",
    "duplicate_of_source_id" => nil,
    "approved_summary_ref" => nil,
    "normalized_knowledge_refs" => [],
    "candidate_record_refs" => [],
    "field_evidence_refs" => [],
    "derived_classification" => "pending",
    "review_status" => "proposed"
  }
end

used_sequences = Hash.new { |hash, key| hash[key] = [] }
existing_records.each do |record|
  prefix, sequence = record.fetch("source_id").match(/\A(SRC-[A-Z]{2,4})-(\d{6})\z/).captures
  used_sequences[prefix] << sequence.to_i
end

entries.group_by { |entry| entry.fetch("source_category") }.each do |category, category_entries|
  prefix = prefixes.fetch(category)
  next_sequence = used_sequences[prefix].max.to_i + 1
  category_entries.sort_by { |entry| entry.fetch("current_relative_path") }.each do |entry|
    next if entry["source_id"]

    entry["source_id"] = format("%s-%06d", prefix, next_sequence)
    next_sequence += 1
  end
end

duplicate_primary_path = "strategic_intent/vision/the-innovation-advantage-genai-cant-give-you.pdf"
duplicate_secondary_path = "use_cases/general_use/the-innovation-advantage-genai-cant-give-you.pdf"
primary = entries.find { |entry| entry.fetch("current_relative_path") == duplicate_primary_path }
secondary = entries.find { |entry| entry.fetch("current_relative_path") == duplicate_secondary_path }
if primary && secondary
  secondary["duplicate_status"] = "suspected"
  secondary["duplicate_of_source_id"] = primary.fetch("source_id")
  secondary["handling_notes"] = "Metadata-only duplicate candidate; retain independently until an approved local hash comparison."
end

entries.group_by { |entry| [entry.fetch("size_bytes"), entry.fetch("filesystem_modified_at")] }.each_value do |matches|
  next unless matches.length > 1
  next if matches.any? { |entry| entry.fetch("duplicate_status") == "suspected" }

  primary_entry, *candidate_entries = matches.sort_by { |entry| entry.fetch("source_id") }
  candidate_entries.each do |candidate|
    next if candidate.fetch("duplicate_status") == "suspected"

    candidate["duplicate_status"] = "suspected"
    candidate["duplicate_of_source_id"] = primary_entry.fetch("source_id")
    candidate["handling_notes"] = "Metadata-only duplicate candidate based on matching size and modification timestamp; retain independently until an approved local hash comparison."
  end
end

output = {
  "schema_version" => 1,
  "register" => "sources",
  "records" => entries.sort_by { |entry| entry.fetch("source_id") }
}

yaml = YAML.dump(output).lines.map do |line|
  line.end_with?(": \n") ? line.sub(": \n", ": null\n") : line
end.join
print yaml
