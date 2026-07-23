#!/usr/bin/env bash

set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
asset_root="$root/assets/marketing/prototypes/visual-sprint-zero"
metadata="$asset_root/metadata.yaml"

directions=(
  "$asset_root/direction-01-transit.svg"
  "$asset_root/direction-02-human-editorial.svg"
  "$asset_root/direction-03-wayfinding.svg"
  "$asset_root/direction-04-modular.svg"
  "$asset_root/direction-05-executive.svg"
  "$asset_root/direction-06-hybrid.svg"
)

xml_assets=("$asset_root/canonical-pay-code-object.svg" "${directions[@]}")

for asset in "${xml_assets[@]}"; do
  xmllint --noout "$asset"
  rg -q '<title id="title">' "$asset"
  rg -q '<desc id="desc">' "$asset"
  rg -q '7K9M-4R2P' "$asset"
  rg -q 'data-role="parallel-frame"' "$asset"

  if rg -o '#[0-9A-Fa-f]{6}' "$asset" | rg -qv '^#(111111|333333|444444|555555|777777|888888|999999|aaaaaa|bbbbbb|dddddd|eeeeee|f4f4f4|fafafa|ffffff)$'; then
    echo "Non-grayscale color found in $asset" >&2
    exit 1
  fi
done

for asset in "${directions[@]}"; do
  object_count="$(rg -o 'data-object="pay-code"' "$asset" | wc -l | tr -d ' ')"
  frame_count="$(rg -o 'data-role="parallel-frame"' "$asset" | wc -l | tr -d ' ')"
  code_count="$(rg -o '>7K9M-4R2P<' "$asset" | wc -l | tr -d ' ')"

  test "$object_count" -eq 3
  test "$frame_count" -eq 3
  test "$code_count" -eq 3
done

ruby -e '
  require "yaml"
  data = YAML.load_file(ARGV.fetch(0))
  abort "wrong sprint state" unless data["status"] == "nonproduction_exploration"
  abort "wrong canonical object" unless data.dig("canonical_object", "illustrative_value") == "7K9M-4R2P"
  abort "direction count mismatch" unless data.fetch("directions").length == 6
  abort "production identity selected" unless data["production_identity_selected"] == false
  abort "RV-001 boundary missing" unless data.dig("validation", "rv_001_affected") == false
' "$metadata"

git -C "$root" diff --quiet HEAD -- assets/marketing/prototypes/milestone-5 assets/marketing/prototypes/milestone-5.1

echo "Visual Sprint Zero validation passed."
