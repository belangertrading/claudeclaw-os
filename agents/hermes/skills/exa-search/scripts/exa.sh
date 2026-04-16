#!/bin/bash
# Exa.ai API wrapper

set -e

API_KEY="${EXA_API_KEY:-}"
BASE_URL="https://api.exa.ai"

if [[ -z "$API_KEY" ]]; then
    echo "Error: EXA_API_KEY environment variable not set" >&2
    echo "Get your free API key at: https://dashboard.exa.ai/api-keys" >&2
    exit 1
fi

usage() {
    cat << EOF
Usage: exa.sh <command> [args] [options]

Commands:
  search <query>     Search the web
  crawl <url>        Get content from a URL
  company <domain>   Research a company
  similar <url>      Find similar sites

Options:
  --num <n>          Number of results (default: 10)
  --text             Include page content
  --type <type>      Search type: auto, neural, keyword (default: auto)

Examples:
  exa.sh search "AI startups" --text --num 5
  exa.sh crawl "https://example.com"
  exa.sh company "stripe.com"
EOF
    exit 1
}

# Parse command
COMMAND="${1:-}"
shift || usage

case "$COMMAND" in
    search)
        QUERY="${1:-}"
        shift || true
        
        [[ -z "$QUERY" ]] && { echo "Error: Query required" >&2; exit 1; }
        
        NUM=10
        TEXT=false
        TYPE="auto"
        
        while [[ $# -gt 0 ]]; do
            case "$1" in
                --num) NUM="$2"; shift 2 ;;
                --text) TEXT=true; shift ;;
                --type) TYPE="$2"; shift 2 ;;
                *) shift ;;
            esac
        done
        
        BODY=$(cat << EOF
{
    "query": "$QUERY",
    "numResults": $NUM,
    "type": "$TYPE",
    "text": $TEXT
}
EOF
)
        curl -s -X POST "$BASE_URL/search" \
            -H "Content-Type: application/json" \
            -H "x-api-key: $API_KEY" \
            -d "$BODY"
        ;;
        
    crawl)
        URL="${1:-}"
        [[ -z "$URL" ]] && { echo "Error: URL required" >&2; exit 1; }
        
        BODY=$(cat << EOF
{
    "urls": ["$URL"],
    "text": true
}
EOF
)
        curl -s -X POST "$BASE_URL/contents" \
            -H "Content-Type: application/json" \
            -H "x-api-key: $API_KEY" \
            -d "$BODY"
        ;;
        
    company)
        DOMAIN="${1:-}"
        [[ -z "$DOMAIN" ]] && { echo "Error: Domain required" >&2; exit 1; }
        
        # Search for company info
        BODY=$(cat << EOF
{
    "query": "site:$DOMAIN",
    "numResults": 10,
    "type": "keyword",
    "text": true
}
EOF
)
        curl -s -X POST "$BASE_URL/search" \
            -H "Content-Type: application/json" \
            -H "x-api-key: $API_KEY" \
            -d "$BODY"
        ;;
        
    similar)
        URL="${1:-}"
        [[ -z "$URL" ]] && { echo "Error: URL required" >&2; exit 1; }
        
        BODY=$(cat << EOF
{
    "url": "$URL",
    "numResults": 10
}
EOF
)
        curl -s -X POST "$BASE_URL/findSimilar" \
            -H "Content-Type: application/json" \
            -H "x-api-key: $API_KEY" \
            -d "$BODY"
        ;;
        
    *)
        usage
        ;;
esac
