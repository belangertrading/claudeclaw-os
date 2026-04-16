# Member Memo — Gotchas

1. **NEVER test the live webhook.** March 17: fired `service="Test"` but N8N filter didn't recognize "Test" — Alliance filter fell through, sent to all Alliance + Titans. The test row in the sheet means nothing if the routing logic doesn't match.

2. **Test the FILTER before testing the SEND.** Verify N8N handles the service name correctly before putting any payload through the webhook.

3. **Alliance filter is permissive by design.** Alliance matches on OI, HMT, 48HC, and Alliance. It does NOT match on "Test" or "Trading Club" or "Titans" (fixed March 17). If you add a new service name, verify it doesn't fall through.

4. **Don't repeat sends.** If an email was already sent (even accidentally), don't resend the same content. Send a short follow-up with only what was missing.

5. **Use Gmail draft to preview formatting, not the webhook.** Save the HTML as an .eml, pipe to himalaya drafts. Review in Gmail. Only webhook when content is approved.

6. **Service hierarchy:** Titans > Alliance > Trading Club > Individual services. Titans get everything. Alliance gets all alerts. Trading Club gets mentorship only.
