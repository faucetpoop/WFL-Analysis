#!/bin/bash
# ==============================================================================
# Validate Gemini-Identified Variables Exist in Survey Data
# ==============================================================================
# Purpose: Check if OP034-OP037 variables exist before adding to YAML
# Date: 2025-11-23
# Usage: bash 01_scripts/validate_gemini_variables.sh

echo "================================================================================"
echo "GEMINI VARIABLE VALIDATION SCRIPT"
echo "================================================================================"
echo ""
echo "Checking if variables identified by Gemini actually exist in your data..."
echo ""

cd "$(dirname "$0")/.." || exit 1  # Go to project root

DATA_DIR="00_inputs/data"
HH_FILE="household_survey_LONG_BIEN_2024_ALL_merged.csv"
VEN_FILE="vendor_survey_LONG_BIEN_2024_ALL_merged.csv"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# ==============================================================================
# HOUSEHOLD SURVEY VALIDATION
# ==============================================================================

echo "📋 HOUSEHOLD SURVEY VARIABLES"
echo "──────────────────────────────────────────────────────────────────────────────"
echo ""

if [ ! -f "$DATA_DIR/$HH_FILE" ]; then
    echo -e "${RED}✗ ERROR: Household survey file not found:${NC}"
    echo "  $DATA_DIR/$HH_FILE"
    echo ""
    echo "Please update HH_FILE variable in this script with correct filename."
    exit 1
fi

# Extract header row
HH_HEADER=$(head -1 "$DATA_DIR/$HH_FILE")

# OP034: Social Food Sharing
echo "OP034: Social Food Sharing Network"
echo "  Looking for: foodsharing_activity_give, foodsharing_activity_receive"
FOODSHARING_GIVE=$(echo "$HH_HEADER" | tr ',' '\n' | grep -i "foodsharing.*give" || echo "")
FOODSHARING_RECEIVE=$(echo "$HH_HEADER" | tr ',' '\n' | grep -i "foodsharing.*receive" || echo "")

if [ -n "$FOODSHARING_GIVE" ] || [ -n "$FOODSHARING_RECEIVE" ]; then
    echo -e "  ${GREEN}✓ FOUND${NC}"
    [ -n "$FOODSHARING_GIVE" ] && echo "    - $FOODSHARING_GIVE"
    [ -n "$FOODSHARING_RECEIVE" ] && echo "    - $FOODSHARING_RECEIVE"
else
    echo -e "  ${RED}✗ NOT FOUND${NC}"
    echo "    Searching for any 'foodsharing' or 'sharing' columns..."
    FOODSHARING_ANY=$(echo "$HH_HEADER" | tr ',' '\n' | grep -i "sharing" || echo "")
    if [ -n "$FOODSHARING_ANY" ]; then
        echo -e "    ${YELLOW}⚠ Found similar:${NC}"
        echo "$FOODSHARING_ANY" | while read -r line; do echo "      - $line"; done
    else
        echo "    No 'sharing' columns found in household survey."
    fi
fi
echo ""

# OP035: Typhoon Preparation
echo "OP035: Typhoon Yagi Preparation (Household)"
echo "  Looking for: typhoon_prepare_* (stockpiling, saving, reducing, etc.)"
TYPHOON_PREP=$(echo "$HH_HEADER" | tr ',' '\n' | grep -i "typhoon.*prep" || echo "")

if [ -n "$TYPHOON_PREP" ]; then
    echo -e "  ${GREEN}✓ FOUND${NC}"
    echo "$TYPHOON_PREP" | head -5 | while read -r line; do echo "    - $line"; done
    PREP_COUNT=$(echo "$TYPHOON_PREP" | wc -l | tr -d ' ')
    if [ "$PREP_COUNT" -gt 5 ]; then
        echo "    ... and $((PREP_COUNT - 5)) more typhoon_prepare columns"
    fi
else
    echo -e "  ${RED}✗ NOT FOUND${NC}"
    echo "    Searching for any 'typhoon' columns..."
    TYPHOON_ANY=$(echo "$HH_HEADER" | tr ',' '\n' | grep -i "typhoon" || echo "")
    if [ -n "$TYPHOON_ANY" ]; then
        echo -e "    ${YELLOW}⚠ Found typhoon columns:${NC}"
        echo "$TYPHOON_ANY" | head -5 | while read -r line; do echo "      - $line"; done
    else
        echo "    No 'typhoon' columns found in household survey."
    fi
fi
echo ""

# OP036: Typhoon Coping
echo "OP036: Typhoon Yagi Coping Strategies (Household)"
echo "  Looking for: typhoon_cope_*"
TYPHOON_COPE=$(echo "$HH_HEADER" | tr ',' '\n' | grep -i "typhoon.*cope" || echo "")

if [ -n "$TYPHOON_COPE" ]; then
    echo -e "  ${GREEN}✓ FOUND${NC}"
    echo "$TYPHOON_COPE" | head -5 | while read -r line; do echo "    - $line"; done
    COPE_COUNT=$(echo "$TYPHOON_COPE" | wc -l | tr -d ' ')
    if [ "$COPE_COUNT" -gt 5 ]; then
        echo "    ... and $((COPE_COUNT - 5)) more typhoon_cope columns"
    fi
else
    echo -e "  ${YELLOW}⚠ NOT FOUND (may be same as OP035)${NC}"
fi
echo ""

# OPTIONAL: Food Waste
echo "OP038 (OPTIONAL): Food Waste"
echo "  Looking for: foodwaste_amount, foodwaste_mainreason"
FOODWASTE=$(echo "$HH_HEADER" | tr ',' '\n' | grep -i "foodwaste\|food.*waste" || echo "")

if [ -n "$FOODWASTE" ]; then
    echo -e "  ${GREEN}✓ FOUND${NC}"
    echo "$FOODWASTE" | while read -r line; do echo "    - $line"; done
else
    echo -e "  ${RED}✗ NOT FOUND${NC}"
fi
echo ""

# ==============================================================================
# VENDOR SURVEY VALIDATION
# ==============================================================================

echo ""
echo "🏪 VENDOR SURVEY VARIABLES"
echo "──────────────────────────────────────────────────────────────────────────────"
echo ""

if [ ! -f "$DATA_DIR/$VEN_FILE" ]; then
    echo -e "${RED}✗ ERROR: Vendor survey file not found:${NC}"
    echo "  $DATA_DIR/$VEN_FILE"
    echo ""
    echo "Please update VEN_FILE variable in this script with correct filename."
    exit 1
fi

# Extract header row
VEN_HEADER=$(head -1 "$DATA_DIR/$VEN_FILE")

# OP037: Vendor Recovery
echo "OP037: Vendor Recovery Capacity (Typhoon Yagi)"
echo "  Looking for: typhoon_damages, typhoon_financial, typhoon_impact"
VENDOR_TYPHOON=$(echo "$VEN_HEADER" | tr ',' '\n' | grep -i "typhoon" || echo "")

if [ -n "$VENDOR_TYPHOON" ]; then
    echo -e "  ${GREEN}✓ FOUND${NC}"
    echo "$VENDOR_TYPHOON" | while read -r line; do echo "    - $line"; done
else
    echo -e "  ${RED}✗ NOT FOUND${NC}"
    echo "    No 'typhoon' columns found in vendor survey."
fi
echo ""

# ==============================================================================
# SUMMARY & RECOMMENDATIONS
# ==============================================================================

echo ""
echo "================================================================================"
echo "VALIDATION SUMMARY"
echo "================================================================================"
echo ""

# Count findings
FOUND_COUNT=0
MISSING_COUNT=0

[ -n "$FOODSHARING_GIVE" ] || [ -n "$FOODSHARING_RECEIVE" ] && FOUND_COUNT=$((FOUND_COUNT + 1)) || MISSING_COUNT=$((MISSING_COUNT + 1))
[ -n "$TYPHOON_PREP" ] && FOUND_COUNT=$((FOUND_COUNT + 1)) || MISSING_COUNT=$((MISSING_COUNT + 1))
[ -n "$VENDOR_TYPHOON" ] && FOUND_COUNT=$((FOUND_COUNT + 1)) || MISSING_COUNT=$((MISSING_COUNT + 1))

echo "Variables Found:   $FOUND_COUNT / 3 (core variables)"
echo "Variables Missing: $MISSING_COUNT / 3"
echo ""

if [ $FOUND_COUNT -eq 3 ]; then
    echo -e "${GREEN}✓ RECOMMENDATION: PROCEED WITH ADDING OP034-OP037 TO YAML${NC}"
    echo ""
    echo "All core variables exist in your data. You can safely:"
    echo "  1. Add OP034-OP037 to operationalization_master.yaml"
    echo "  2. Add construction functions to phase_1_CORRECTED_variable_construction.py"
    echo "  3. Re-run Phase 1 processing"
    echo ""
    echo "See: claudedocs/GEMINI_MASTER_TABLE_VS_YAML_COMPARISON.md"
    echo "     (Section: YAML Enhancement Recommendation)"
elif [ $FOUND_COUNT -ge 2 ]; then
    echo -e "${YELLOW}⚠ RECOMMENDATION: PARTIAL IMPLEMENTATION POSSIBLE${NC}"
    echo ""
    echo "Most variables exist. Consider adding the found operationalizations."
    echo "For missing variables, document as 'planned_only' in YAML."
    echo ""
elif [ $FOUND_COUNT -eq 1 ]; then
    echo -e "${YELLOW}⚠ RECOMMENDATION: SELECTIVE IMPLEMENTATION${NC}"
    echo ""
    echo "Only some variables found. Add what exists, document rest as limitation."
else
    echo -e "${RED}✗ RECOMMENDATION: DO NOT PROCEED${NC}"
    echo ""
    echo "Core variables not found in data. Possibilities:"
    echo "  1. Variable names in data differ from Gemini's assumptions"
    echo "  2. These sections were in ODK survey but not collected"
    echo "  3. Data file names in this script are incorrect"
    echo ""
    echo "Next steps:"
    echo "  - Manually inspect: $DATA_DIR/$HH_FILE (first row)"
    echo "  - Check ODK survey instruments for actual variable names"
    echo "  - Update this script with correct variable patterns"
fi

echo ""
echo "================================================================================"
echo "For detailed analysis and implementation guide, see:"
echo "  claudedocs/GEMINI_ANALYSIS_EXECUTIVE_SUMMARY.md"
echo "================================================================================"
echo ""
