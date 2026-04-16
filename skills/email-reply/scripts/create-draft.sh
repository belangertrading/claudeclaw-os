#!/bin/bash
# Create a Gmail draft reply threaded to the original email
# Usage: ./create-draft.sh <to> <subject> <reply-to-message-id> <body> [from]

TO="$1"
SUBJECT="$2"
REPLY_TO_ID="$3"
BODY="$4"
FROM="${5:-Josh@joshbelanger.com}"

if [ -z "$TO" ] || [ -z "$SUBJECT" ] || [ -z "$REPLY_TO_ID" ] || [ -z "$BODY" ]; then
  echo "Usage: ./create-draft.sh <to> <subject> <reply-to-message-id> <body> [from]"
  exit 1
fi

GOG_KEYRING_PASSWORD="henrybot2026" gog gmail draft create \
  --to "$TO" \
  --subject "$SUBJECT" \
  --reply-to-message-id "$REPLY_TO_ID" \
  --from "$FROM" \
  --body "$BODY"
