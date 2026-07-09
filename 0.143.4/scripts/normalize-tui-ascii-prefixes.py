diff --git a/codex-rs/tui/src/app/agent_status_feed.rs b/codex-rs/tui/src/app/agent_status_feed.rs
index eb14551d5a..eff1ab43e5 100644
--- a/codex-rs/tui/src/app/agent_status_feed.rs
+++ b/codex-rs/tui/src/app/agent_status_feed.rs
@@ -38,7 +38,7 @@ impl HistoryCell for AgentStatusHistoryCell {
         ];
 
         if self.entries.is_empty() {
-            lines.push("  • No sub-agents running.".italic().into());
+            lines.push("  ■ No sub-agents running.".italic().into());
             return lines;
         }
 
@@ -114,7 +114,7 @@ impl AgentStatusThreadPreview {
     }
 
     fn title_line(&self) -> Line<'static> {
-        vec!["  • ".dim(), format!("`{}`", self.agent_path).cyan()].into()
+        vec!["  ■ ".dim(), format!("`{}`", self.agent_path).cyan()].into()
     }
 
     fn preview_lines(&self, width: u16) -> Vec<Line<'static>> {
diff --git a/codex-rs/tui/src/app/agent_status_feed_tests.rs b/codex-rs/tui/src/app/agent_status_feed_tests.rs
index d7583d2b44..b62aafac51 100644
--- a/codex-rs/tui/src/app/agent_status_feed_tests.rs
+++ b/codex-rs/tui/src/app/agent_status_feed_tests.rs
@@ -55,7 +55,7 @@ fn agent_status_uses_bounded_buffered_activity() {
     /agent
     Sub-agents running
 
-      • `/root/reviewer`
+      ■ `/root/reviewer`
         $ cargo test -p codex-tui
         Finished checking the focused TUI tests.
     "###);
@@ -103,7 +103,7 @@ fn agent_status_uses_reasoning_summaries_only() {
     /agent
     Sub-agents running
 
-      • `/root/reviewer`
+      ■ `/root/reviewer`
         safe summary
     "###);
     assert!(!rendered.contains("hidden raw reasoning"));
diff --git a/codex-rs/tui/src/app/event_dispatch.rs b/codex-rs/tui/src/app/event_dispatch.rs
index afe269195a..153dd059e8 100644
--- a/codex-rs/tui/src/app/event_dispatch.rs
+++ b/codex-rs/tui/src/app/event_dispatch.rs
@@ -1473,7 +1473,7 @@ impl App {
                                     self.chat_widget.submit_initial_user_message_if_pending();
                                 }
                                 self.chat_widget.add_plain_history_lines(vec![
-                                    Line::from(vec!["• ".dim(), "Sandbox ready".into()]),
+                                    Line::from(vec!["■ ".dim(), "Sandbox ready".into()]),
                                     Line::from(vec![
                                         "  ".into(),
                                         "Codex can now safely edit files and execute commands in your computer"
@@ -1506,7 +1506,7 @@ impl App {
                                         preset.active_permission_profile.clone(),
                                     ));
                                 self.chat_widget.add_plain_history_lines(vec![
-                                    Line::from(vec!["• ".dim(), "Sandbox ready".into()]),
+                                    Line::from(vec!["■ ".dim(), "Sandbox ready".into()]),
                                     Line::from(vec![
                                         "  ".into(),
                                         "Codex can now safely edit files and execute commands in your computer"
diff --git a/codex-rs/tui/src/app/snapshots/codex_tui__app__history_ui__tests__desktop_thread_opened_history.snap b/codex-rs/tui/src/app/snapshots/codex_tui__app__history_ui__tests__desktop_thread_opened_history.snap
index a1f5264511..9c93e2fe02 100644
--- a/codex-rs/tui/src/app/snapshots/codex_tui__app__history_ui__tests__desktop_thread_opened_history.snap
+++ b/codex-rs/tui/src/app/snapshots/codex_tui__app__history_ui__tests__desktop_thread_opened_history.snap
@@ -2,4 +2,4 @@
 source: tui/src/app/history_ui_tests.rs
 expression: render_cell(&cell)
 ---
-• Opened this session in Codex Desktop.
+■ Opened this session in Codex Desktop.
diff --git a/codex-rs/tui/src/app/startup_prompts.rs b/codex-rs/tui/src/app/startup_prompts.rs
index 55a377ec11..3952126a1f 100644
--- a/codex-rs/tui/src/app/startup_prompts.rs
+++ b/codex-rs/tui/src/app/startup_prompts.rs
@@ -517,8 +517,8 @@ mod tests {
         .join("\n");
 
         insta::assert_snapshot!(rendered, @r"
-⚠ Skipped loading 1 skill(s) due to invalid SKILL.md files.
-⚠ /repo/.codex/skills/abc/SKILL.md: invalid description
+! Skipped loading 1 skill(s) due to invalid SKILL.md files.
+! /repo/.codex/skills/abc/SKILL.md: invalid description
 ");
     }
 }
diff --git a/codex-rs/tui/src/app/tests.rs b/codex-rs/tui/src/app/tests.rs
index d8d63575bb..02e801a4bb 100644
--- a/codex-rs/tui/src/app/tests.rs
+++ b/codex-rs/tui/src/app/tests.rs
@@ -2627,7 +2627,7 @@ async fn inactive_thread_file_change_approval_recovers_buffered_changes() {
         other => panic!("expected patch preview history cell, saw {other:?}"),
     };
     let rendered = lines_to_single_string(&cell.display_lines(/*width*/ 80));
-    assert!(rendered.contains("• Added README.md (+1 -0)"));
+    assert!(rendered.contains("■ Added README.md (+1 -0)"));
     assert!(rendered.contains("1 +hello"));
 }
 
@@ -4814,7 +4814,7 @@ async fn feedback_submission_for_inactive_thread_replays_into_origin_thread() {
         }
     }
     assert!(rendered_cells.iter().any(|cell| {
-        cell.contains("• Feedback uploaded. Please open an issue using the following URL:")
+        cell.contains("■ Feedback uploaded. Please open an issue using the following URL:")
             && cell.contains("uploaded-thread")
     }));
 }
diff --git a/codex-rs/tui/src/app_backtrack.rs b/codex-rs/tui/src/app_backtrack.rs
index 0870093883..0ee22b3f9f 100644
--- a/codex-rs/tui/src/app_backtrack.rs
+++ b/codex-rs/tui/src/app_backtrack.rs
@@ -807,7 +807,7 @@ mod tests {
             .iter()
             .map(|span| span.content.as_ref())
             .collect();
-        assert_eq!(intro_text, "• intro");
+        assert_eq!(intro_text, "■ intro");
     }
 
     #[test]
@@ -851,7 +851,7 @@ mod tests {
             .iter()
             .map(|span| span.content.as_ref())
             .collect();
-        assert_eq!(intro_text, "• intro");
+        assert_eq!(intro_text, "■ intro");
 
         let user_first = cells[1]
             .as_any()
@@ -942,7 +942,7 @@ mod tests {
             .iter()
             .map(|span| span.content.as_ref())
             .collect();
-        assert_eq!(intro_text, "• intro");
+        assert_eq!(intro_text, "■ intro");
     }
 
     #[test]
diff --git a/codex-rs/tui/src/bottom_pane/approval_overlay.rs b/codex-rs/tui/src/bottom_pane/approval_overlay.rs
index 3cc135da74..e3c17945bd 100644
--- a/codex-rs/tui/src/bottom_pane/approval_overlay.rs
+++ b/codex-rs/tui/src/bottom_pane/approval_overlay.rs
@@ -2219,7 +2219,7 @@ mod tests {
             })
             .collect();
         let expected = vec![
-            "✔ You approved codex to run".to_string(),
+            "+ You approved codex to run".to_string(),
             "  git add tui/src/render/".to_string(),
             "  mod.rs tui/src/render/".to_string(),
             "  renderable.rs this time".to_string(),
@@ -2236,7 +2236,7 @@ mod tests {
         );
         assert_eq!(
             render_history_cell_lines(approved.as_ref(), /*width*/ 80),
-            vec!["✔ You approved this request this time".to_string()]
+            vec!["+ You approved this request this time".to_string()]
         );
 
         let approved_for_session = history_cell::new_approval_decision_cell(
@@ -2246,7 +2246,7 @@ mod tests {
         );
         assert_eq!(
             render_history_cell_lines(approved_for_session.as_ref(), /*width*/ 80),
-            vec!["✔ You approved this request every time this session".to_string()]
+            vec!["+ You approved this request every time this session".to_string()]
         );
     }
 
@@ -2289,7 +2289,7 @@ mod tests {
         assert_eq!(
             render_history_cell_lines(decision.as_ref(), /*width*/ 80),
             vec![
-                "✔ You approved codex network access to https://example.com:8443 this time"
+                "+ You approved codex network access to https://example.com:8443 this time"
                     .to_string(),
             ]
         );
diff --git a/codex-rs/tui/src/bottom_pane/feedback_view.rs b/codex-rs/tui/src/bottom_pane/feedback_view.rs
index ce380a867d..1f1e8dab46 100644
--- a/codex-rs/tui/src/bottom_pane/feedback_view.rs
+++ b/codex-rs/tui/src/bottom_pane/feedback_view.rs
@@ -315,9 +315,9 @@ pub(crate) fn feedback_success_cell(
     feedback_audience: FeedbackAudience,
 ) -> history_cell::WebHyperlinkHistoryCell {
     let prefix = if include_logs {
-        "• Feedback uploaded."
+        "■ Feedback uploaded."
     } else {
-        "• Feedback recorded (no logs)."
+        "■ Feedback recorded (no logs)."
     };
     let issue_url = issue_url_for_category(category, thread_id, feedback_audience);
     let mut lines = vec![Line::from(match issue_url.as_ref() {
@@ -504,9 +504,9 @@ pub(crate) fn feedback_upload_consent_params(
         Line::from("Upload logs?".bold()).into(),
         Line::from("").into(),
         Line::from("The following files will be sent:".dim()).into(),
-        Line::from(vec!["  • ".into(), "codex-logs.log".into()]).into(),
+        Line::from(vec!["  ■ ".into(), "codex-logs.log".into()]).into(),
         Line::from(vec![
-            "  • ".into(),
+            "  ■ ".into(),
             DOCTOR_REPORT_ATTACHMENT_FILENAME.into(),
         ])
         .into(),
@@ -514,7 +514,7 @@ pub(crate) fn feedback_upload_consent_params(
     if include_windows_sandbox_log {
         header_lines.push(
             Line::from(vec![
-                "  • ".into(),
+                "  ■ ".into(),
                 WINDOWS_SANDBOX_LOG_ATTACHMENT_FILENAME.into(),
             ])
             .into(),
@@ -523,15 +523,15 @@ pub(crate) fn feedback_upload_consent_params(
     if let Some(path) = rollout_path.as_deref()
         && let Some(name) = path.file_name().map(|s| s.to_string_lossy().to_string())
     {
-        header_lines.push(Line::from(vec!["  • ".into(), name.into()]).into());
+        header_lines.push(Line::from(vec!["  ■ ".into(), name.into()]).into());
     }
     if let Some(filename) = auto_review_rollout_filename {
-        header_lines.push(Line::from(vec!["  • ".into(), filename.into()]).into());
+        header_lines.push(Line::from(vec!["  ■ ".into(), filename.into()]).into());
     }
     if !feedback_diagnostics.is_empty() {
         header_lines.push(
             Line::from(vec![
-                "  • ".into(),
+                "  ■ ".into(),
                 FEEDBACK_DIAGNOSTICS_ATTACHMENT_FILENAME.into(),
             ])
             .into(),
@@ -872,7 +872,7 @@ mod tests {
         );
         assert_eq!(
             rendered,
-            "• Feedback uploaded. Please open an issue using the following URL:\n\n  https://github.com/openai/codex/issues/new?template=3-cli.yml&steps=Uploaded%20thread:%20thread-1\n\n  Or mention your thread ID thread-1 in an existing issue."
+            "■ Feedback uploaded. Please open an issue using the following URL:\n\n  https://github.com/openai/codex/issues/new?template=3-cli.yml&steps=Uploaded%20thread:%20thread-1\n\n  Or mention your thread ID thread-1 in an existing issue."
         );
     }
 
@@ -889,7 +889,7 @@ mod tests {
         );
         assert_eq!(
             rendered,
-            "• Feedback uploaded. Please report this in #codex-feedback:\n\n  http://go/codex-feedback-internal\n\n  Share this and add some info about your problem:\n    https://go/codex-feedback/thread-2"
+            "■ Feedback uploaded. Please report this in #codex-feedback:\n\n  http://go/codex-feedback-internal\n\n  Share this and add some info about your problem:\n    https://go/codex-feedback/thread-2"
         );
     }
 
@@ -906,7 +906,7 @@ mod tests {
         );
         assert_eq!(
             rendered,
-            "• Feedback recorded (no logs). Thanks for the feedback!\n\n  Thread ID: thread-3"
+            "■ Feedback recorded (no logs). Thanks for the feedback!\n\n  Thread ID: thread-3"
         );
     }
 
diff --git a/codex-rs/tui/src/bottom_pane/hooks_browser_view.rs b/codex-rs/tui/src/bottom_pane/hooks_browser_view.rs
index bd6e25f7ca..dd3690c0d0 100644
--- a/codex-rs/tui/src/bottom_pane/hooks_browser_view.rs
+++ b/codex-rs/tui/src/bottom_pane/hooks_browser_view.rs
@@ -398,7 +398,7 @@ impl HooksBrowserView {
             self.entry
                 .warnings
                 .iter()
-                .map(|warning| format!("⚠ {warning}").into()),
+                .map(|warning| format!("! {warning}").into()),
         );
         lines.extend(self.entry.errors.iter().map(|error| {
             format!("■ {}: {}", error.path.display(), error.message)
@@ -414,7 +414,7 @@ impl HooksBrowserView {
         lines.push(Line::default());
 
         if let Some(message) = review_needed_message(self.review_needed_total_count()) {
-            lines.push(format!("⚠ {message}").yellow().into());
+            lines.push(format!("! {message}").yellow().into());
             lines.push(Line::default());
         }
 
diff --git a/codex-rs/tui/src/bottom_pane/mod.rs b/codex-rs/tui/src/bottom_pane/mod.rs
index ad30dedf5a..c8446cbe92 100644
--- a/codex-rs/tui/src/bottom_pane/mod.rs
+++ b/codex-rs/tui/src/bottom_pane/mod.rs
@@ -2379,7 +2379,7 @@ mod tests {
         pane.render(area, &mut buf);
 
         let bufs = snapshot_buffer(&buf);
-        assert!(bufs.contains("• Working"), "expected Working header");
+        assert!(bufs.contains("■ Working"), "expected Working header");
     }
 
     #[test]
diff --git a/codex-rs/tui/src/bottom_pane/pending_input_preview.rs b/codex-rs/tui/src/bottom_pane/pending_input_preview.rs
index 96cc1bdfd8..8d870143a3 100644
--- a/codex-rs/tui/src/bottom_pane/pending_input_preview.rs
+++ b/codex-rs/tui/src/bottom_pane/pending_input_preview.rs
@@ -68,7 +68,7 @@ impl PendingInputPreview {
     }
 
     fn push_section_header(lines: &mut Vec<Line<'static>>, width: u16, header: Line<'static>) {
-        let mut spans = vec!["• ".dim()];
+        let mut spans = vec!["■ ".dim()];
         spans.extend(header.spans);
         lines.extend(adaptive_wrap_lines(
             std::iter::once(Line::from(spans)),
@@ -102,7 +102,7 @@ impl PendingInputPreview {
                 let wrapped = adaptive_wrap_lines(
                     steer.lines().map(|line| Line::from(line.dim())),
                     RtOptions::new(width as usize)
-                        .initial_indent(Line::from("  ↳ ".dim()))
+                        .initial_indent(Line::from("  > ".dim()))
                         .subsequent_indent(Line::from("    ")),
                 );
                 Self::push_truncated_preview_lines(&mut lines, wrapped, Line::from("    …".dim()));
@@ -123,7 +123,7 @@ impl PendingInputPreview {
                 let wrapped = adaptive_wrap_lines(
                     steer.lines().map(|line| Line::from(line.dim())),
                     RtOptions::new(width as usize)
-                        .initial_indent(Line::from("  ↳ ".dim()))
+                        .initial_indent(Line::from("  > ".dim()))
                         .subsequent_indent(Line::from("    ")),
                 );
                 Self::push_truncated_preview_lines(&mut lines, wrapped, Line::from("    …".dim()));
@@ -140,7 +140,7 @@ impl PendingInputPreview {
                 let wrapped = adaptive_wrap_lines(
                     message.lines().map(|line| Line::from(line.dim().italic())),
                     RtOptions::new(width as usize)
-                        .initial_indent(Line::from("  ↳ ".dim()))
+                        .initial_indent(Line::from("  > ".dim()))
                         .subsequent_indent(Line::from("    ")),
                 );
                 Self::push_truncated_preview_lines(
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__chat_composer__tests__footer_mode_shortcut_overlay.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__chat_composer__tests__footer_mode_shortcut_overlay.snap
index 5239a34bd2..7c144cd8dd 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__chat_composer__tests__footer_mode_shortcut_overlay.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__chat_composer__tests__footer_mode_shortcut_overlay.snap
@@ -15,7 +15,7 @@ expression: terminal.backend()
 "  @ for file paths                           ctrl + v to paste images                               "
 "  ctrl + g to edit in external editor        esc again to edit previous message                     "
 "  ctrl + r search history                    ctrl + c to exit                                       "
-"  ⌥ + , reasoning down                       ⌥ + . reasoning up                                     "
+"  - + , reasoning down                       - + . reasoning up                                     "
 "  ctrl + t to view transcript                                                                       "
 "                                                                                                    "
 "  customize shortcuts with /keymap                                                                  "
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__chat_composer__tests__footer_mode_shortcut_overlay_queue_submissions.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__chat_composer__tests__footer_mode_shortcut_overlay_queue_submissions.snap
index 582724eea7..58ab1fea82 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__chat_composer__tests__footer_mode_shortcut_overlay_queue_submissions.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__chat_composer__tests__footer_mode_shortcut_overlay_queue_submissions.snap
@@ -15,7 +15,7 @@ expression: terminal.backend()
 "  @ for file paths                           ctrl + v to paste images                               "
 "  ctrl + g to edit in external editor        esc esc to edit previous message                       "
 "  ctrl + r search history                    ctrl + c to exit                                       "
-"  ⌥ + , reasoning down                       ⌥ + . reasoning up                                     "
+"  - + , reasoning down                       - + . reasoning up                                     "
 "  ctrl + t to view transcript                                                                       "
 "                                                                                                    "
 "  customize shortcuts with /keymap                                                                  "
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__feedback_view__tests__feedback_upload_consent_lists_doctor_report.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__feedback_view__tests__feedback_upload_consent_lists_doctor_report.snap
index e91d736ecd..ebeb63b29d 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__feedback_view__tests__feedback_upload_consent_lists_doctor_report.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__feedback_view__tests__feedback_upload_consent_lists_doctor_report.snap
@@ -6,7 +6,7 @@ expression: rendered
 Upload logs?
 
 The following files will be sent:
-  • codex-logs.log
-  • codex-doctor-report.json
-  • rollout.jsonl
-  • auto-review-rollout.jsonl
+  ■ codex-logs.log
+  ■ codex-doctor-report.json
+  ■ rollout.jsonl
+  ■ auto-review-rollout.jsonl
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__feedback_view__tests__feedback_upload_consent_lists_windows_sandbox_log_when_included.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__feedback_view__tests__feedback_upload_consent_lists_windows_sandbox_log_when_included.snap
index 741505d5f5..11500303cc 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__feedback_view__tests__feedback_upload_consent_lists_windows_sandbox_log_when_included.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__feedback_view__tests__feedback_upload_consent_lists_windows_sandbox_log_when_included.snap
@@ -6,8 +6,8 @@ expression: rendered
 Upload logs?
 
 The following files will be sent:
-  • codex-logs.log
-  • codex-doctor-report.json
-  • windows-sandbox.log
-  • rollout.jsonl
-  • auto-review-rollout.jsonl
+  ■ codex-logs.log
+  ■ codex-doctor-report.json
+  ■ windows-sandbox.log
+  ■ rollout.jsonl
+  ■ auto-review-rollout.jsonl
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__footer__tests__footer_shortcuts_collaboration_modes_enabled.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__footer__tests__footer_shortcuts_collaboration_modes_enabled.snap
index 3b67a90683..4c0a7a2149 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__footer__tests__footer_shortcuts_collaboration_modes_enabled.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__footer__tests__footer_shortcuts_collaboration_modes_enabled.snap
@@ -7,7 +7,7 @@ expression: terminal.backend()
 "  @ for file paths                           ctrl + v to paste images           "
 "  ctrl + g to edit in external editor        esc esc to edit previous message   "
 "  ctrl + r search history                    ctrl + c to exit                   "
-"  ⌥ + , reasoning down                       ⌥ + . reasoning up                 "
+"  - + , reasoning down                       - + . reasoning up                 "
 "  shift + tab to change mode                 ctrl + t to view transcript        "
 "                                                                                "
 "  customize shortcuts with /keymap                                              "
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__footer__tests__footer_shortcuts_running.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__footer__tests__footer_shortcuts_running.snap
index 7c733bd13b..c053440fea 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__footer__tests__footer_shortcuts_running.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__footer__tests__footer_shortcuts_running.snap
@@ -7,7 +7,7 @@ expression: terminal.backend()
 "  @ for file paths                           ctrl + v to paste images           "
 "  ctrl + g to edit in external editor        esc esc to edit previous message   "
 "  ctrl + r search history                    ctrl + c to interrupt              "
-"  ⌥ + , reasoning down                       ⌥ + . reasoning up                 "
+"  - + , reasoning down                       - + . reasoning up                 "
 "  ctrl + t to view transcript                                                   "
 "                                                                                "
 "  customize shortcuts with /keymap                                              "
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__footer__tests__footer_shortcuts_shift_and_esc.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__footer__tests__footer_shortcuts_shift_and_esc.snap
index 07e9706283..212bef834c 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__footer__tests__footer_shortcuts_shift_and_esc.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__footer__tests__footer_shortcuts_shift_and_esc.snap
@@ -7,7 +7,7 @@ expression: terminal.backend()
 "  @ for file paths                           ctrl + v to paste images           "
 "  ctrl + g to edit in external editor        esc again to edit previous message "
 "  ctrl + r search history                    ctrl + c to exit                   "
-"  ⌥ + , reasoning down                       ⌥ + . reasoning up                 "
+"  - + , reasoning down                       - + . reasoning up                 "
 "  ctrl + t to view transcript                                                   "
 "                                                                                "
 "  customize shortcuts with /keymap                                              "
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__hooks_browser_view__tests__hooks_browser_events_with_issues.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__hooks_browser_view__tests__hooks_browser_events_with_issues.snap
index 7dc71463dc..5948996ec7 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__hooks_browser_view__tests__hooks_browser_events_with_issues.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__hooks_browser_view__tests__hooks_browser_events_with_issues.snap
@@ -7,7 +7,7 @@ expression: "render_lines(&view, 112)"
   Lifecycle hooks from config and enabled plugins.                                                              
                                                                                                                 
   Issues                                                                                                        
-  ⚠ skipped invalid matcher for PreToolUse                                                                      
+  ! skipped invalid matcher for PreToolUse                                                                      
   ■ /tmp/hooks.json: failed to parse hooks config                                                               
                                                                                                                 
   Event                 Installed   Active      Description                                                     
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__hooks_browser_view__tests__hooks_browser_events_with_review_column.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__hooks_browser_view__tests__hooks_browser_events_with_review_column.snap
index c18657d8a1..fc385a502c 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__hooks_browser_view__tests__hooks_browser_events_with_review_column.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__hooks_browser_view__tests__hooks_browser_events_with_review_column.snap
@@ -6,7 +6,7 @@ expression: "render_lines(&view, 112)"
   Hooks                                                                                                         
   Lifecycle hooks from config and enabled plugins.                                                              
                                                                                                                 
-  ⚠ 1 hook needs review before it can run.                                                                      
+  ! 1 hook needs review before it can run.                                                                      
                                                                                                                 
   Event                 Installed   Active      Review      Description                                         
   PreToolUse            1           0           1           Before a tool executes                              
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__message_queue__tests__render_many_line_message.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__message_queue__tests__render_many_line_message.snap
index cf1f7248b3..53420c666f 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__message_queue__tests__render_many_line_message.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__message_queue__tests__render_many_line_message.snap
@@ -5,7 +5,7 @@ expression: "format!(\"{buf:?}\")"
 Buffer {
     area: Rect { x: 0, y: 0, width: 40, height: 5 },
     content: [
-        "  ↳ This is                             ",
+        "  > This is                             ",
         "    a message                           ",
         "    with many                           ",
         "    …                                   ",
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__message_queue__tests__render_one_message.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__message_queue__tests__render_one_message.snap
index 5e403e1bdd..d6636de5bd 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__message_queue__tests__render_one_message.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__message_queue__tests__render_one_message.snap
@@ -5,7 +5,7 @@ expression: "format!(\"{buf:?}\")"
 Buffer {
     area: Rect { x: 0, y: 0, width: 40, height: 2 },
     content: [
-        "  ↳ Hello, world!                       ",
+        "  > Hello, world!                       ",
         "    alt + ↑ edit                        ",
     ],
     styles: [
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__message_queue__tests__render_two_messages.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__message_queue__tests__render_two_messages.snap
index 4484509695..34b50a17be 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__message_queue__tests__render_two_messages.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__message_queue__tests__render_two_messages.snap
@@ -5,8 +5,8 @@ expression: "format!(\"{buf:?}\")"
 Buffer {
     area: Rect { x: 0, y: 0, width: 40, height: 3 },
     content: [
-        "  ↳ Hello, world!                       ",
-        "  ↳ This is another message             ",
+        "  > Hello, world!                       ",
+        "  > This is another message             ",
         "    alt + ↑ edit                        ",
     ],
     styles: [
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__message_queue__tests__render_wrapped_message.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__message_queue__tests__render_wrapped_message.snap
index 16d6361257..c8e363967d 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__message_queue__tests__render_wrapped_message.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__message_queue__tests__render_wrapped_message.snap
@@ -5,9 +5,9 @@ expression: "format!(\"{buf:?}\")"
 Buffer {
     area: Rect { x: 0, y: 0, width: 40, height: 4 },
     content: [
-        "  ↳ This is a longer message that should",
+        "  > This is a longer message that should",
         "    be wrapped                          ",
-        "  ↳ This is another message             ",
+        "  > This is another message             ",
         "    alt + ↑ edit                        ",
     ],
     styles: [
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_many_line_message.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_many_line_message.snap
index 65c011c26b..4347fe0c2f 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_many_line_message.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_many_line_message.snap
@@ -6,12 +6,12 @@ expression: "format!(\"{buf:?}\")"
 Buffer {
     area: Rect { x: 0, y: 0, width: 40, height: 6 },
     content: [
-        "• Queued follow-up inputs               ",
-        "  ↳ This is                             ",
+        "■ Queued follow-up inputs               ",
+        "  > This is                             ",
         "    a message                           ",
         "    with many                           ",
         "    …                                   ",
-        "    ⌥ + ↑ edit last queued message      ",
+        "    - + ↑ edit last queued message      ",
     ],
     styles: [
         x: 0, y: 0, fg: Reset, bg: Reset, underline: Reset, modifier: DIM,
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_more_than_three_messages.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_more_than_three_messages.snap
index f2506a3646..5b2fd15505 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_more_than_three_messages.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_more_than_three_messages.snap
@@ -6,12 +6,12 @@ expression: "format!(\"{buf:?}\")"
 Buffer {
     area: Rect { x: 0, y: 0, width: 40, height: 6 },
     content: [
-        "• Queued follow-up inputs               ",
-        "  ↳ Hello, world!                       ",
-        "  ↳ This is another message             ",
-        "  ↳ This is a third message             ",
-        "  ↳ This is a fourth message            ",
-        "    ⌥ + ↑ edit last queued message      ",
+        "■ Queued follow-up inputs               ",
+        "  > Hello, world!                       ",
+        "  > This is another message             ",
+        "  > This is a third message             ",
+        "  > This is a fourth message            ",
+        "    - + ↑ edit last queued message      ",
     ],
     styles: [
         x: 0, y: 0, fg: Reset, bg: Reset, underline: Reset, modifier: DIM,
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_multiline_pending_steer_uses_single_prefix_and_truncates.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_multiline_pending_steer_uses_single_prefix_and_truncates.snap
index be89f767a8..7df728dd4b 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_multiline_pending_steer_uses_single_prefix_and_truncates.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_multiline_pending_steer_uses_single_prefix_and_truncates.snap
@@ -5,9 +5,9 @@ expression: "format!(\"{buf:?}\")"
 Buffer {
     area: Rect { x: 0, y: 0, width: 48, height: 6 },
     content: [
-        "• Messages to be submitted after next tool call ",
+        "■ Messages to be submitted after next tool call ",
         "  (press esc to interrupt and send immediately) ",
-        "  ↳ First line                                  ",
+        "  > First line                                  ",
         "    Second line                                 ",
         "    Third line                                  ",
         "    …                                           ",
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_one_message.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_one_message.snap
index 74e39ed514..d84d6fd09c 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_one_message.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_one_message.snap
@@ -6,9 +6,9 @@ expression: "format!(\"{buf:?}\")"
 Buffer {
     area: Rect { x: 0, y: 0, width: 40, height: 3 },
     content: [
-        "• Queued follow-up inputs               ",
-        "  ↳ Hello, world!                       ",
-        "    ⌥ + ↑ edit last queued message      ",
+        "■ Queued follow-up inputs               ",
+        "  > Hello, world!                       ",
+        "    - + ↑ edit last queued message      ",
     ],
     styles: [
         x: 0, y: 0, fg: Reset, bg: Reset, underline: Reset, modifier: DIM,
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_one_message_with_shift_left_binding.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_one_message_with_shift_left_binding.snap
index c79ee32506..0a255ceab1 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_one_message_with_shift_left_binding.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_one_message_with_shift_left_binding.snap
@@ -6,8 +6,8 @@ expression: "format!(\"{buf:?}\")"
 Buffer {
     area: Rect { x: 0, y: 0, width: 40, height: 3 },
     content: [
-        "• Queued follow-up inputs               ",
-        "  ↳ Hello, world!                       ",
+        "■ Queued follow-up inputs               ",
+        "  > Hello, world!                       ",
         "    shift + ← edit last queued message  ",
     ],
     styles: [
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_one_pending_steer.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_one_pending_steer.snap
index 9a8e3b96d1..c88520ffd2 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_one_pending_steer.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_one_pending_steer.snap
@@ -5,9 +5,9 @@ expression: "format!(\"{buf:?}\")"
 Buffer {
     area: Rect { x: 0, y: 0, width: 48, height: 3 },
     content: [
-        "• Messages to be submitted after next tool call ",
+        "■ Messages to be submitted after next tool call ",
         "  (press esc to interrupt and send immediately) ",
-        "  ↳ Please continue.                            ",
+        "  > Please continue.                            ",
     ],
     styles: [
         x: 0, y: 0, fg: Reset, bg: Reset, underline: Reset, modifier: DIM,
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_one_pending_steer_with_remapped_interrupt_binding.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_one_pending_steer_with_remapped_interrupt_binding.snap
index f8a3caa1bf..43f591ce02 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_one_pending_steer_with_remapped_interrupt_binding.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_one_pending_steer_with_remapped_interrupt_binding.snap
@@ -5,9 +5,9 @@ expression: "format!(\"{buf:?}\")"
 Buffer {
     area: Rect { x: 0, y: 0, width: 48, height: 3 },
     content: [
-        "• Messages to be submitted after next tool call ",
+        "■ Messages to be submitted after next tool call ",
         "  (press f12 to interrupt and send immediately) ",
-        "  ↳ Please continue.                            ",
+        "  > Please continue.                            ",
     ],
     styles: [
         x: 0, y: 0, fg: Reset, bg: Reset, underline: Reset, modifier: DIM,
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_pending_steers_above_queued_messages.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_pending_steers_above_queued_messages.snap
index 0321b79d6b..e29c517601 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_pending_steers_above_queued_messages.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_pending_steers_above_queued_messages.snap
@@ -6,17 +6,17 @@ expression: "format!(\"{buf:?}\")"
 Buffer {
     area: Rect { x: 0, y: 0, width: 52, height: 11 },
     content: [
-        "• Messages to be submitted after next tool call     ",
+        "■ Messages to be submitted after next tool call     ",
         "  (press esc to interrupt and send immediately)     ",
-        "  ↳ Please continue.                                ",
-        "  ↳ Check the last command output.                  ",
+        "  > Please continue.                                ",
+        "  > Check the last command output.                  ",
         "                                                    ",
-        "• Messages to be submitted at end of turn           ",
-        "  ↳ Rejected steer that will be retried.            ",
+        "■ Messages to be submitted at end of turn           ",
+        "  > Rejected steer that will be retried.            ",
         "                                                    ",
-        "• Queued follow-up inputs                           ",
-        "  ↳ Queued follow-up question                       ",
-        "    ⌥ + ↑ edit last queued message                  ",
+        "■ Queued follow-up inputs                           ",
+        "  > Queued follow-up question                       ",
+        "    - + ↑ edit last queued message                  ",
     ],
     styles: [
         x: 0, y: 0, fg: Reset, bg: Reset, underline: Reset, modifier: DIM,
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_two_messages.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_two_messages.snap
index 90c4fea4a0..cd8861b4b5 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_two_messages.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_two_messages.snap
@@ -6,10 +6,10 @@ expression: "format!(\"{buf:?}\")"
 Buffer {
     area: Rect { x: 0, y: 0, width: 40, height: 4 },
     content: [
-        "• Queued follow-up inputs               ",
-        "  ↳ Hello, world!                       ",
-        "  ↳ This is another message             ",
-        "    ⌥ + ↑ edit last queued message      ",
+        "■ Queued follow-up inputs               ",
+        "  > Hello, world!                       ",
+        "  > This is another message             ",
+        "    - + ↑ edit last queued message      ",
     ],
     styles: [
         x: 0, y: 0, fg: Reset, bg: Reset, underline: Reset, modifier: DIM,
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_wrapped_message.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_wrapped_message.snap
index b338f880ac..ddbf377c6e 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_wrapped_message.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__pending_input_preview__tests__render_wrapped_message.snap
@@ -6,11 +6,11 @@ expression: "format!(\"{buf:?}\")"
 Buffer {
     area: Rect { x: 0, y: 0, width: 40, height: 5 },
     content: [
-        "• Queued follow-up inputs               ",
-        "  ↳ This is a longer message that should",
+        "■ Queued follow-up inputs               ",
+        "  > This is a longer message that should",
         "    be wrapped                          ",
-        "  ↳ This is another message             ",
-        "    ⌥ + ↑ edit last queued message      ",
+        "  > This is another message             ",
+        "    - + ↑ edit last queued message      ",
     ],
     styles: [
         x: 0, y: 0, fg: Reset, bg: Reset, underline: Reset, modifier: DIM,
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__tests__queued_messages_visible_when_status_hidden_snapshot.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__tests__queued_messages_visible_when_status_hidden_snapshot.snap
index dbaad63442..887b050f66 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__tests__queued_messages_visible_when_status_hidden_snapshot.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__tests__queued_messages_visible_when_status_hidden_snapshot.snap
@@ -3,9 +3,9 @@ source: tui/src/bottom_pane/mod.rs
 assertion_line: 1858
 expression: "render_snapshot(&pane, area)"
 ---
-• Queued follow-up inputs                       
-  ↳ Queued follow-up question                   
-    ⌥ + ↑ edit last queued message              
+■ Queued follow-up inputs                       
+  > Queued follow-up question                   
+    - + ↑ edit last queued message              
                                                 
 › Ask Codex to do anything                      
                                                 
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__tests__status_and_composer_fill_height_without_bottom_padding.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__tests__status_and_composer_fill_height_without_bottom_padding.snap
index 5c95c9f811..4bb5442715 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__tests__status_and_composer_fill_height_without_bottom_padding.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__tests__status_and_composer_fill_height_without_bottom_padding.snap
@@ -2,7 +2,7 @@
 source: tui/src/bottom_pane/mod.rs
 expression: "render_snapshot(&pane, area)"
 ---
-• Working (0s • esc to interr…
+■ Working (0s ■ esc to interr…
                               
                               
 › Ask Codex to do anything    
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__tests__status_and_queued_messages_snapshot.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__tests__status_and_queued_messages_snapshot.snap
index 94f462d835..95a83d1e34 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__tests__status_and_queued_messages_snapshot.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__tests__status_and_queued_messages_snapshot.snap
@@ -3,11 +3,11 @@ source: tui/src/bottom_pane/mod.rs
 assertion_line: 1889
 expression: "render_snapshot(&pane, area)"
 ---
-• Working (0s • esc to interrupt)               
+■ Working (0s ■ esc to interrupt)               
                                                 
-• Queued follow-up inputs                       
-  ↳ Queued follow-up question                   
-    ⌥ + ↑ edit last queued message              
+■ Queued follow-up inputs                       
+  > Queued follow-up question                   
+    - + ↑ edit last queued message              
                                                 
 › Ask Codex to do anything                      
                                                 
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__tests__status_only_snapshot.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__tests__status_only_snapshot.snap
index 136c358055..1948e0fe3f 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__tests__status_only_snapshot.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__tests__status_only_snapshot.snap
@@ -2,7 +2,7 @@
 source: tui/src/bottom_pane/mod.rs
 expression: "render_snapshot(&pane, area)"
 ---
-• Working (0s • esc to interrupt)               
+■ Working (0s ■ esc to interrupt)               
                                                 
                                                 
 › Ask Codex to do anything                      
diff --git a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__tests__status_with_details_and_queued_messages_snapshot.snap b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__tests__status_with_details_and_queued_messages_snapshot.snap
index 4e8763c83d..bea280b123 100644
--- a/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__tests__status_with_details_and_queued_messages_snapshot.snap
+++ b/codex-rs/tui/src/bottom_pane/snapshots/codex_tui__bottom_pane__tests__status_with_details_and_queued_messages_snapshot.snap
@@ -3,13 +3,13 @@ source: tui/src/bottom_pane/mod.rs
 assertion_line: 1826
 expression: "render_snapshot(&pane, area)"
 ---
-• Working (0s • esc to interrupt)               
+■ Working (0s ■ esc to interrupt)               
   └ First detail line                           
     Second detail line                          
                                                 
-• Queued follow-up inputs                       
-  ↳ Queued follow-up question                   
-    ⌥ + ↑ edit last queued message              
+■ Queued follow-up inputs                       
+  > Queued follow-up question                   
+    - + ↑ edit last queued message              
                                                 
 › Ask Codex to do anything                      
                                                 
diff --git a/codex-rs/tui/src/bottom_pane/textarea.rs b/codex-rs/tui/src/bottom_pane/textarea.rs
index f727ca3480..3a1f7af7f8 100644
--- a/codex-rs/tui/src/bottom_pane/textarea.rs
+++ b/codex-rs/tui/src/bottom_pane/textarea.rs
@@ -2013,7 +2013,7 @@ mod tests {
             46..=52 => (rng.random_range(b'0'..=b'9') as char).to_string(),
             53..=65 => {
                 // Some emoji (wide graphemes)
-                let choices = ["👍", "😊", "🐍", "🚀", "🧪", "🌟"];
+                let choices = ["*", "*", "*", "*", "*", "*"];
                 choices[rng.random_range(0..choices.len())].to_string()
             }
             66..=75 => {
@@ -2029,15 +2029,15 @@ mod tests {
             }
             86..=92 => {
                 // Some non-latin single codepoints (Greek, Cyrillic, Hebrew)
-                let choices = ["Ω", "β", "Ж", "ю", "ש", "م", "ह"];
+                let choices = ["Ω", "β", "Ж", "ю", "ש", "م", "?"];
                 choices[rng.random_range(0..choices.len())].to_string()
             }
             _ => {
                 // ZWJ sequences (single graphemes but multi-codepoint)
                 let choices = [
-                    "👩\u{200D}💻", // woman technologist
-                    "👨\u{200D}💻", // man technologist
-                    "🏳️\u{200D}🌈", // rainbow flag
+                    "*\u{200D}*", // woman technologist
+                    "*\u{200D}*", // man technologist
+                    "*\u{200D}*", // rainbow flag
                 ];
                 choices[rng.random_range(0..choices.len())].to_string()
             }
@@ -2227,7 +2227,7 @@ mod tests {
 
     #[test]
     fn vim_escape_moves_by_grapheme_boundary() {
-        let mut t = ta_with("👍👍");
+        let mut t = ta_with("**");
         t.set_cursor(t.text().len());
         t.set_vim_enabled(/*enabled*/ true);
 
@@ -2235,7 +2235,7 @@ mod tests {
         t.input(KeyEvent::new(KeyCode::Esc, KeyModifiers::NONE));
 
         assert_eq!(t.vim_mode_label(), Some("Normal"));
-        assert_eq!(t.cursor(), "👍".len());
+        assert_eq!(t.cursor(), "*".len());
     }
 
     #[test]
@@ -2981,12 +2981,12 @@ mod tests {
 
     #[test]
     fn cursor_left_and_right_handle_graphemes() {
-        let mut t = ta_with("a👍b");
+        let mut t = ta_with("a*b");
         t.set_cursor(t.text().len());
 
         t.move_cursor_left(); // before 'b'
         let after_first_left = t.cursor();
-        t.move_cursor_left(); // before '👍'
+        t.move_cursor_left(); // before '*'
         let after_second_left = t.cursor();
         t.move_cursor_left(); // before 'a'
         let after_third_left = t.cursor();
@@ -3587,21 +3587,21 @@ mod tests {
     #[test]
     fn wrapped_navigation_with_wide_graphemes() {
         // Four thumbs up, each of display width 2, with width 3 to force wrapping inside grapheme boundaries
-        let mut t = ta_with("👍👍👍👍");
+        let mut t = ta_with("****");
         let _ = t.desired_height(/*width*/ 3);
 
         // Put cursor after the second emoji (which should be on first wrapped line)
-        t.set_cursor("👍👍".len());
+        t.set_cursor("**".len());
 
         // Move down should go to the start of the next wrapped line (same column preserved but clamped)
         t.move_cursor_down();
         // We expect to land somewhere within the third emoji or at the start of it
         let pos_after_down = t.cursor();
-        assert!(pos_after_down >= "👍👍".len());
+        assert!(pos_after_down >= "**".len());
 
         // Moving up should take us back to the original position
         t.move_cursor_up();
-        assert_eq!(t.cursor(), "👍👍".len());
+        assert_eq!(t.cursor(), "**".len());
     }
 
     #[test]
diff --git a/codex-rs/tui/src/chatwidget.rs b/codex-rs/tui/src/chatwidget.rs
index 42903d2e7f..509d7a844e 100644
--- a/codex-rs/tui/src/chatwidget.rs
+++ b/codex-rs/tui/src/chatwidget.rs
@@ -1413,7 +1413,7 @@ impl ChatWidget {
         self.transcript.bump_active_cell_revision();
     }
 
-    /// Mark the active cell as failed (✗) and flush it into history.
+    /// Mark the active cell as failed (x) and flush it into history.
     fn finalize_active_cell_as_failed(&mut self) {
         if let Some(mut cell) = self.transcript.active_cell.take() {
             // Insert finalized cell into history and keep grouping consistent.
@@ -1566,7 +1566,7 @@ impl ChatWidget {
 
     fn rename_confirmation_cell(name: &str, thread_id: Option<ThreadId>) -> PlainHistoryCell {
         let mut line = vec![
-            "• ".into(),
+            "■ ".into(),
             "Session renamed to ".into(),
             name.to_string().cyan(),
         ];
diff --git a/codex-rs/tui/src/chatwidget/model_popups.rs b/codex-rs/tui/src/chatwidget/model_popups.rs
index 1194fc15c6..2816dd6aa3 100644
--- a/codex-rs/tui/src/chatwidget/model_popups.rs
+++ b/codex-rs/tui/src/chatwidget/model_popups.rs
@@ -369,7 +369,7 @@ impl ChatWidget {
         };
         let warning_text = warn_effort.as_ref().map(|effort| {
             let effort_label = Self::reasoning_effort_label(effort);
-            format!("⚠ {effort_label} reasoning effort can quickly consume Plus plan rate limits.")
+            format!("! {effort_label} reasoning effort can quickly consume Plus plan rate limits.")
         });
         let warn_for_model = preset.model.starts_with("gpt-5.1-codex")
             || preset.model.starts_with("gpt-5.1-codex-max")
diff --git a/codex-rs/tui/src/chatwidget/session_flow.rs b/codex-rs/tui/src/chatwidget/session_flow.rs
index 177700d4f4..6d913a21a5 100644
--- a/codex-rs/tui/src/chatwidget/session_flow.rs
+++ b/codex-rs/tui/src/chatwidget/session_flow.rs
@@ -186,7 +186,7 @@ impl ChatWidget {
             && !name.trim().is_empty()
         {
             vec![
-                "• ".dim(),
+                "■ ".dim(),
                 "Thread forked from ".into(),
                 name.cyan(),
                 " (".into(),
@@ -196,7 +196,7 @@ impl ChatWidget {
             .into()
         } else {
             vec![
-                "• ".dim(),
+                "■ ".dim(),
                 "Thread forked from ".into(),
                 forked_from_id_text.cyan(),
             ]
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_collab_spawn_completed_renders_requested_model_and_effort.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_collab_spawn_completed_renders_requested_model_and_effort.snap
index 0b5eeed1af..934aadbe16 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_collab_spawn_completed_renders_requested_model_and_effort.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_collab_spawn_completed_renders_requested_model_and_effort.snap
@@ -2,5 +2,5 @@
 source: tui/src/chatwidget/tests.rs
 expression: combined
 ---
-• Spawned 019cff70-2599-75e2-af72-b91781b41a8e (gpt-5 high)
+■ Spawned 019cff70-2599-75e2-af72-b91781b41a8e (gpt-5 high)
   └ Explore the repo
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_collab_wait_items_render_history.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_collab_wait_items_render_history.snap
index 21eaf5207b..448374f1da 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_collab_wait_items_render_history.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_collab_wait_items_render_history.snap
@@ -2,11 +2,11 @@
 source: tui/src/chatwidget/tests.rs
 expression: combined
 ---
-• Waiting for 2 agents
+■ Waiting for 2 agents
   └ Robie [explorer]
     Ada [reviewer]
 
 
-• Finished waiting
+■ Finished waiting
   └ Robie [explorer]: Completed - Done
     Ada [reviewer]: Running
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_forked_thread_history_line.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_forked_thread_history_line.snap
index 2b4e8bc029..3657878f3d 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_forked_thread_history_line.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_forked_thread_history_line.snap
@@ -2,4 +2,4 @@
 source: tui/src/chatwidget/tests/history_replay.rs
 expression: combined
 ---
-• Thread forked from app-server-parent-thread (e9f18a88-8081-4e51-9d4e-8af5cde2d8dd)
+■ Thread forked from app-server-parent-thread (e9f18a88-8081-4e51-9d4e-8af5cde2d8dd)
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_forked_thread_history_line_without_app_server_name.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_forked_thread_history_line_without_app_server_name.snap
index cd092d4760..23f4a3f7cc 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_forked_thread_history_line_without_app_server_name.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_forked_thread_history_line_without_app_server_name.snap
@@ -2,4 +2,4 @@
 source: tui/src/chatwidget/tests/history_replay.rs
 expression: combined
 ---
-• Thread forked from 019c2d47-4935-7423-a190-05691f566092
+■ Thread forked from 019c2d47-4935-7423-a190-05691f566092
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_guardian_review_denied_renders_denied_request.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_guardian_review_denied_renders_denied_request.snap
index 70af203e46..bc3aeca694 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_guardian_review_denied_renders_denied_request.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_guardian_review_denied_renders_denied_request.snap
@@ -9,10 +9,10 @@ expression: normalize_snapshot_paths(term.backend().vt100().screen().contents())
 
 
 
-✗ Request denied for codex to run curl -sS -i -X POST --data-binary
+x Request denied for codex to run curl -sS -i -X POST --data-binary
   @core/src/codex.rs https://example.com
 
-• Working (0s • esc to interrupt)
+■ Working (0s ■ esc to interrupt)
 
 
 › Ask Codex to do anything
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_guardian_review_timed_out_renders_timed_out_request.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_guardian_review_timed_out_renders_timed_out_request.snap
index 3dfe36e763..120bdfc18b 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_guardian_review_timed_out_renders_timed_out_request.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_guardian_review_timed_out_renders_timed_out_request.snap
@@ -9,10 +9,10 @@ expression: normalize_snapshot_paths(term.backend().vt100().screen().contents())
 
 
 
-✗ Review timed out before codex could run curl -sS -i -X POST --data-binary
+x Review timed out before codex could run curl -sS -i -X POST --data-binary
   @core/src/codex.rs https://example.com
 
-• Working (0s • esc to interrupt)
+■ Working (0s ■ esc to interrupt)
 
 
 › Ask Codex to do anything
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_mcp_startup_failure_renders_warning_history.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_mcp_startup_failure_renders_warning_history.snap
index efc431bbe8..49a6db4e9d 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_mcp_startup_failure_renders_warning_history.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__app_server_mcp_startup_failure_renders_warning_history.snap
@@ -5,8 +5,8 @@ expression: normalize_snapshot_paths(term.backend().vt100().screen().contents())
 
 
 
-⚠ MCP client for `alpha` failed to start: handshake failed
-⚠ MCP startup incomplete (failed: alpha)
+! MCP client for `alpha` failed to start: handshake failed
+! MCP startup incomplete (failed: alpha)
 
 
 › Ask Codex to do anything
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__apply_patch_manual_flow_history_approved.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__apply_patch_manual_flow_history_approved.snap
index e139b51088..8746d97c40 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__apply_patch_manual_flow_history_approved.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__apply_patch_manual_flow_history_approved.snap
@@ -2,5 +2,5 @@
 source: tui/src/chatwidget/tests.rs
 expression: lines_to_single_string(&approved_lines)
 ---
-• Added foo.txt (+1 -0)
+■ Added foo.txt (+1 -0)
     1 +hello
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__binary_size_ideal_response.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__binary_size_ideal_response.snap
index 38fb05e28d..0b4f3a4849 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__binary_size_ideal_response.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__binary_size_ideal_response.snap
@@ -2,7 +2,7 @@
 source: tui/src/chatwidget/tests.rs
 expression: "lines[start_idx..].join(\"\\n\")"
 ---
-• I need to check the codex-rs repository to explain why the project's binaries
+■ I need to check the codex-rs repository to explain why the project's binaries
   are large. The user is likely seeking specifics about the setup: are Rust
   builds static, what features are enabled, and is debug information included?
   It could be due to static linking, included OpenSSL, or how panic handling
@@ -11,14 +11,14 @@ expression: "lines[start_idx..].join(\"\\n\")"
 
 ─ Worked for 0s ────────────────────────────────────────────────────────────────
 
-• I’m going to scan the workspace and Cargo manifests to see build profiles and
+■ I’m going to scan the workspace and Cargo manifests to see build profiles and
   dependencies that impact binary size. Then I’ll summarize the main causes.
 
-• Explored
+■ Explored
   └ List ls -la
     Read Cargo.toml
 
-• I'm reviewing the workspace's release profile, which has settings like
+■ I'm reviewing the workspace's release profile, which has settings like
   lto=fat, strip=symbols, and codegen-units=1 to reduce binary size. However, it
   seems that "strip = symbols" only removes symbols, not debug information. In
   Rust 1.73+, both "symbols" and "debuginfo" stripping options are available. I
@@ -26,7 +26,7 @@ expression: "lines[start_idx..].join(\"\\n\")"
   through crates for heavy dependencies in Cargo.toml, including cli, core,
   exec, linux-sandbox, tui, login, ollama, and mcp.
 
-• Ran for d in ansi-escape apply-patch arg0 cli common core exec execpolicy
+■ Ran for d in ansi-escape apply-patch arg0 cli common core exec execpolicy
   │ file-search linux-sandbox login mcp-client mcp-server ollama
   │ tui; do echo "--- $d/Cargo.toml"; sed -n '1,200p' $d/Cargo.toml; echo;
   │ … +1 lines
@@ -36,10 +36,10 @@ expression: "lines[start_idx..].join(\"\\n\")"
     ] }
     tracing = { version
 
-• Explored
+■ Explored
   └ Read Cargo.toml
 
-• I’m evaluating how binary size is influenced by various factors. There are
+■ I’m evaluating how binary size is influenced by various factors. There are
   many binaries, such as codex and codex-exec, which include dependencies by
   default, pulling in features like Tokio and hyper. For instance, reqwest
   includes default features like TLS through rustls. If default features remain
@@ -114,7 +114,7 @@ expression: "lines[start_idx..].join(\"\\n\")"
 
 ─ Worked for 0s ────────────────────────────────────────────────────────────────
 
-• Here’s what’s driving size in this workspace’s binaries.
+■ Here’s what’s driving size in this workspace’s binaries.
 
   Main Causes
 
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__chatwidget_exec_and_status_layout_vt100_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__chatwidget_exec_and_status_layout_vt100_snapshot.snap
index dfcfae199f..88d549b84d 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__chatwidget_exec_and_status_layout_vt100_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__chatwidget_exec_and_status_layout_vt100_snapshot.snap
@@ -29,14 +29,14 @@ expression: normalize_snapshot_paths(term.backend().vt100().screen().contents())
 
 
 
-• I’m going to search the repo for where “Change Approved” is rendered to update
+■ I’m going to search the repo for where “Change Approved” is rendered to update
   that view.
 
-• Explored
+■ Explored
   └ Search Change Approved
     Read diff_render.rs
 
-• Investigating rendering code (0s • esc to interrupt)
+■ Investigating rendering code (0s ■ esc to interrupt)
 
 
 › Summarize recent commits
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__chatwidget_markdown_code_blocks_vt100_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__chatwidget_markdown_code_blocks_vt100_snapshot.snap
index 8017384f55..75ac9fcde4 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__chatwidget_markdown_code_blocks_vt100_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__chatwidget_markdown_code_blocks_vt100_snapshot.snap
@@ -37,7 +37,7 @@ expression: term.backend().vt100().screen().contents()
 
 
 
-•     -- Indented code block (4 spaces)
+■     -- Indented code block (4 spaces)
       SELECT *
       FROM "users"
       WHERE "email" LIKE '%@example.com';
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__chatwidget_tall.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__chatwidget_tall.snap
index a21401ff95..d84b93b3e0 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__chatwidget_tall.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__chatwidget_tall.snap
@@ -4,25 +4,25 @@ assertion_line: 2288
 expression: normalize_snapshot_paths(term.backend().vt100().screen().contents())
 ---
 
-• Working (0s • esc to interrupt)
+■ Working (0s ■ esc to interrupt)
 
-• Queued follow-up inputs
-  ↳ Hello, world! 0
-  ↳ Hello, world! 1
-  ↳ Hello, world! 2
-  ↳ Hello, world! 3
-  ↳ Hello, world! 4
-  ↳ Hello, world! 5
-  ↳ Hello, world! 6
-  ↳ Hello, world! 7
-  ↳ Hello, world! 8
-  ↳ Hello, world! 9
-  ↳ Hello, world! 10
-  ↳ Hello, world! 11
-  ↳ Hello, world! 12
-  ↳ Hello, world! 13
-  ↳ Hello, world! 14
-  ↳ Hello, world! 15
+■ Queued follow-up inputs
+  > Hello, world! 0
+  > Hello, world! 1
+  > Hello, world! 2
+  > Hello, world! 3
+  > Hello, world! 4
+  > Hello, world! 5
+  > Hello, world! 6
+  > Hello, world! 7
+  > Hello, world! 8
+  > Hello, world! 9
+  > Hello, world! 10
+  > Hello, world! 11
+  > Hello, world! 12
+  > Hello, world! 13
+  > Hello, world! 14
+  > Hello, world! 15
 
 › Ask Codex to do anything
 
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__compact_queues_user_messages_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__compact_queues_user_messages_snapshot.snap
index 777439a1cd..15cc3b0488 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__compact_queues_user_messages_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__compact_queues_user_messages_snapshot.snap
@@ -12,10 +12,10 @@ expression: normalize_snapshot_paths(term.backend().vt100().screen().contents())
 
 
 
-• Working (0s • esc to interrupt)
+■ Working (0s ■ esc to interrupt)
 
-• Messages to be submitted at end of turn
-  ↳ Steer submitted while /compact was running.
+■ Messages to be submitted at end of turn
+  > Steer submitted while /compact was running.
 
 › Ask Codex to do anything
 
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__completed_hook_output_precedes_following_assistant_message_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__completed_hook_output_precedes_following_assistant_message_snapshot.snap
index 5e8360f015..8433b23429 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__completed_hook_output_precedes_following_assistant_message_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__completed_hook_output_precedes_following_assistant_message_snapshot.snap
@@ -5,7 +5,7 @@ expression: "format!(\"active hooks:\\n{}history:\\n{history}\", active_hook_blo
 active hooks:
 <empty>
 history:
-• PreToolUse hook (blocked)
+■ PreToolUse hook (blocked)
   feedback: command blocked by policy
 
-• The hook feedback was applied.
+■ The hook feedback was applied.
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__completed_hook_with_output_flushes_immediately_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__completed_hook_with_output_flushes_immediately_snapshot.snap
index d2673f5400..a22bc6adcb 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__completed_hook_with_output_flushes_immediately_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__completed_hook_with_output_flushes_immediately_snapshot.snap
@@ -4,7 +4,7 @@ expression: "format!(\"{running_snapshot}\\n\\n{completed_snapshot}\")"
 ---
 running
 live hooks:
-• Running PreToolUse hook: checking command
+■ Running PreToolUse hook: checking command
 history:
 <empty>
 
@@ -12,5 +12,5 @@ completed
 live hooks:
 <empty>
 history:
-• PreToolUse hook (blocked)
+■ PreToolUse hook (blocked)
   feedback: command blocked by policy
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__completed_same_id_hook_output_survives_restart_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__completed_same_id_hook_output_survives_restart_snapshot.snap
index ebdca8fc75..a9d047849d 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__completed_same_id_hook_output_survives_restart_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__completed_same_id_hook_output_survives_restart_snapshot.snap
@@ -3,7 +3,7 @@ source: tui/src/chatwidget/tests/status_and_layout.rs
 expression: "format!(\"active hooks:\\n{}history:\\n{history}\", active_hook_blob(&chat))"
 ---
 active hooks:
-• Running Stop hook: checking stop condition
+■ Running Stop hook: checking stop condition
 history:
-• Stop hook (stopped)
+■ Stop hook (stopped)
   stop: continue with more context
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__completed_turn_clears_visible_running_hook.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__completed_turn_clears_visible_running_hook.snap
index e41954e415..24e652a14f 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__completed_turn_clears_visible_running_hook.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__completed_turn_clears_visible_running_hook.snap
@@ -3,6 +3,6 @@ source: tui/src/chatwidget/tests/status_and_layout.rs
 expression: "format!(\"before completion:\\n{before_completion}after completion:\\n{}\",\nactive_hook_blob(&chat))"
 ---
 before completion:
-• Running PostToolUse hook
+■ Running PostToolUse hook
 after completion:
 <empty>
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__deltas_then_same_final_message_are_rendered_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__deltas_then_same_final_message_are_rendered_snapshot.snap
index 4d916a33cc..cfb101f114 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__deltas_then_same_final_message_are_rendered_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__deltas_then_same_final_message_are_rendered_snapshot.snap
@@ -2,4 +2,4 @@
 source: tui/src/chatwidget/tests/status_and_layout.rs
 expression: combined
 ---
-• Here is the result.
+■ Here is the result.
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__esc_interrupt_goal_paused_footer.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__esc_interrupt_goal_paused_footer.snap
index bebbb3ffd5..7baf379ca9 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__esc_interrupt_goal_paused_footer.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__esc_interrupt_goal_paused_footer.snap
@@ -3,7 +3,7 @@ source: tui/src/chatwidget/tests/status_and_layout.rs
 expression: snapshot
 ---
 "                                                                                "
-"• Working (0s • esc to interrupt)                                               "
+"■ Working (0s ■ esc to interrupt)                                               "
 "                                                                                "
 "                                                                                "
 "› Ask Codex to do anything                                                      "
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__esc_interrupt_goal_paused_footer@windows.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__esc_interrupt_goal_paused_footer@windows.snap
index 1025ae3862..af1378aecc 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__esc_interrupt_goal_paused_footer@windows.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__esc_interrupt_goal_paused_footer@windows.snap
@@ -3,7 +3,7 @@ source: tui/src/chatwidget/tests/status_and_layout.rs
 expression: snapshot
 ---
 "                                                                                "
-"• Working (0s • esc to interrupt)                                               "
+"■ Working (0s ■ esc to interrupt)                                               "
 "                                                                                "
 "                                                                                "
 "› Ask Codex to do anything                                                      "
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exec_approval_history_decision_aborted_long.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exec_approval_history_decision_aborted_long.snap
index c9f305093a..1f03dde2b5 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exec_approval_history_decision_aborted_long.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exec_approval_history_decision_aborted_long.snap
@@ -3,5 +3,5 @@ source: tui/src/chatwidget/tests/exec_flow.rs
 assertion_line: 217
 expression: lines_to_single_string(&aborted_long)
 ---
-✗ You canceled the request to run echo
+x You canceled the request to run echo
   aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa...
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exec_approval_history_decision_aborted_multiline.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exec_approval_history_decision_aborted_multiline.snap
index 4280a39a3a..223b0dc797 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exec_approval_history_decision_aborted_multiline.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exec_approval_history_decision_aborted_multiline.snap
@@ -3,4 +3,4 @@ source: tui/src/chatwidget/tests/exec_flow.rs
 assertion_line: 183
 expression: lines_to_single_string(&aborted_multi)
 ---
-✗ You canceled the request to run echo line1 ...
+x You canceled the request to run echo line1 ...
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exec_approval_history_decision_approved_short.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exec_approval_history_decision_approved_short.snap
index 0a474df75f..920bdead65 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exec_approval_history_decision_approved_short.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exec_approval_history_decision_approved_short.snap
@@ -3,4 +3,4 @@ source: tui/src/chatwidget/tests/exec_flow.rs
 assertion_line: 47
 expression: lines_to_single_string(&decision)
 ---
-✔ You approved codex to run echo hello world this time
++ You approved codex to run echo hello world this time
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step1_start_ls.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step1_start_ls.snap
index a69fccd302..34cf718bd3 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step1_start_ls.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step1_start_ls.snap
@@ -2,5 +2,5 @@
 source: tui/src/chatwidget/tests.rs
 expression: active_blob(&chat)
 ---
-• Exploring
+■ Exploring
   └ List ls -la
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step2_finish_ls.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step2_finish_ls.snap
index e7155b8453..0c5652ca9a 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step2_finish_ls.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step2_finish_ls.snap
@@ -2,5 +2,5 @@
 source: tui/src/chatwidget/tests.rs
 expression: active_blob(&chat)
 ---
-• Explored
+■ Explored
   └ List ls -la
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step3_start_cat_foo.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step3_start_cat_foo.snap
index 6ff2edef8e..473d7f84b0 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step3_start_cat_foo.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step3_start_cat_foo.snap
@@ -2,6 +2,6 @@
 source: tui/src/chatwidget/tests.rs
 expression: active_blob(&chat)
 ---
-• Exploring
+■ Exploring
   └ List ls -la
     Read foo.txt
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step4_finish_cat_foo.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step4_finish_cat_foo.snap
index de15e7ca24..fcf3cf68c8 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step4_finish_cat_foo.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step4_finish_cat_foo.snap
@@ -2,6 +2,6 @@
 source: tui/src/chatwidget/tests.rs
 expression: active_blob(&chat)
 ---
-• Explored
+■ Explored
   └ List ls -la
     Read foo.txt
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step5_finish_sed_range.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step5_finish_sed_range.snap
index de15e7ca24..fcf3cf68c8 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step5_finish_sed_range.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step5_finish_sed_range.snap
@@ -2,6 +2,6 @@
 source: tui/src/chatwidget/tests.rs
 expression: active_blob(&chat)
 ---
-• Explored
+■ Explored
   └ List ls -la
     Read foo.txt
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step6_finish_cat_bar.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step6_finish_cat_bar.snap
index 2a8ed11b7f..3c0f121db0 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step6_finish_cat_bar.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__exploring_step6_finish_cat_bar.snap
@@ -2,6 +2,6 @@
 source: tui/src/chatwidget/tests.rs
 expression: active_blob(&chat)
 ---
-• Explored
+■ Explored
   └ List ls -la
     Read foo.txt, bar.txt
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__failed_image_generation_call_history_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__failed_image_generation_call_history_snapshot.snap
index c69c51f27e..a137079423 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__failed_image_generation_call_history_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__failed_image_generation_call_history_snapshot.snap
@@ -2,5 +2,5 @@
 source: tui/src/chatwidget/tests/exec_flow.rs
 expression: "lines_to_single_string(&cells[0])"
 ---
-✗ Image generation failed
+x Image generation failed
   └ A tiny blue square
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__feedback_good_result_consent_popup.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__feedback_good_result_consent_popup.snap
index cdeedc7b78..9bcc85d189 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__feedback_good_result_consent_popup.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__feedback_good_result_consent_popup.snap
@@ -5,10 +5,10 @@ expression: popup
   Upload logs?
 
   The following files will be sent:
-    • codex-logs.log
-    • codex-doctor-report.json
-    • auto-review-rollout-thread-1.jsonl
-    • codex-connectivity-diagnostics.txt
+    ■ codex-logs.log
+    ■ codex-doctor-report.json
+    ■ auto-review-rollout-thread-1.jsonl
+    ■ codex-connectivity-diagnostics.txt
 
 › 1. Yes  Share the current Codex session logs and diagnostics with the team
           for troubleshooting.
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__feedback_upload_consent_popup.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__feedback_upload_consent_popup.snap
index b860cf8fb3..f6b26473ee 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__feedback_upload_consent_popup.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__feedback_upload_consent_popup.snap
@@ -6,11 +6,11 @@ expression: popup
   Upload logs?
 
   The following files will be sent:
-    • codex-logs.log
-    • codex-doctor-report.json
-    • windows-sandbox.log
-    • auto-review-rollout-thread-1.jsonl
-    • codex-connectivity-diagnostics.txt
+    ■ codex-logs.log
+    ■ codex-doctor-report.json
+    ■ windows-sandbox.log
+    ■ auto-review-rollout-thread-1.jsonl
+    ■ codex-connectivity-diagnostics.txt
 
   Connectivity diagnostics
     - Proxy environment variables are set and may affect connectivity.
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__final_reasoning_then_message_without_deltas_are_rendered.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__final_reasoning_then_message_without_deltas_are_rendered.snap
index 6062087181..4225d66819 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__final_reasoning_then_message_without_deltas_are_rendered.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__final_reasoning_then_message_without_deltas_are_rendered.snap
@@ -2,4 +2,4 @@
 source: tui/src/chatwidget/tests.rs
 expression: combined
 ---
-• Here is the result.
+■ Here is the result.
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__final_worked_for_uses_cumulative_turn_duration.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__final_worked_for_uses_cumulative_turn_duration.snap
index b0d5db920b..bf8458a570 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__final_worked_for_uses_cumulative_turn_duration.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__final_worked_for_uses_cumulative_turn_duration.snap
@@ -2,11 +2,11 @@
 source: tui/src/chatwidget/tests/exec_flow.rs
 expression: combined
 ---
-• Ran echo preparing
+■ Ran echo preparing
   └ preparing
 
 ────────────────────────────────────────────────────────────────────────────────
 
-• Final response.
+■ Final response.
 
 ─ Worked for 2m 05s ────────────────────────────────────────────────────────────
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__foreign_image_attachment_history_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__foreign_image_attachment_history_snapshot.snap
index 1c2102e4ce..6ea89cb809 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__foreign_image_attachment_history_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__foreign_image_attachment_history_snapshot.snap
@@ -3,5 +3,5 @@ source: tui/src/chatwidget/tests/exec_flow.rs
 assertion_line: 877
 expression: combined
 ---
-• Viewed Image
+■ Viewed Image
   └ C:\workspace\assets\example.png
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__forked_thread_history_line.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__forked_thread_history_line.snap
index de72926fd3..fa7e42a24a 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__forked_thread_history_line.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__forked_thread_history_line.snap
@@ -2,4 +2,4 @@
 source: tui/src/chatwidget/tests/history_replay.rs
 expression: combined
 ---
-• Thread forked from named-thread (e9f18a88-8081-4e51-9d4e-8af5cde2d8dd)
+■ Thread forked from named-thread (e9f18a88-8081-4e51-9d4e-8af5cde2d8dd)
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__forked_thread_history_line_without_name.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__forked_thread_history_line_without_name.snap
index f25eb53645..9bcafa0c0e 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__forked_thread_history_line_without_name.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__forked_thread_history_line_without_name.snap
@@ -2,4 +2,4 @@
 source: tui/src/chatwidget/tests.rs
 expression: combined
 ---
-• Thread forked from 019c2d47-4935-7423-a190-05691f566092
+■ Thread forked from 019c2d47-4935-7423-a190-05691f566092
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__guardian_approved_exec_renders_approved_request.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__guardian_approved_exec_renders_approved_request.snap
index 59c2814688..c00ba4a716 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__guardian_approved_exec_renders_approved_request.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__guardian_approved_exec_renders_approved_request.snap
@@ -7,7 +7,7 @@ expression: normalize_snapshot_paths(term.backend().vt100().screen().contents())
 
 
 
-✔ Auto-reviewer approved codex to run rm -f /tmp/guardian-approved.sqlite this
++ Auto-reviewer approved codex to run rm -f /tmp/guardian-approved.sqlite this
   time
 
 
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__guardian_approved_request_permissions_renders_request_summary.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__guardian_approved_request_permissions_renders_request_summary.snap
index 74376286ff..4d589d52e8 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__guardian_approved_request_permissions_renders_request_summary.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__guardian_approved_request_permissions_renders_request_summary.snap
@@ -5,10 +5,10 @@ expression: normalize_snapshot_paths(term.backend().vt100().screen().contents())
 
 
 
-✔ Request approved for permission request: Need write access for generated
++ Request approved for permission request: Need write access for generated
   report assets.
 
-• Working (0s • esc to interrupt)
+■ Working (0s ■ esc to interrupt)
 
 
 › Ask Codex to do anything
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__guardian_denied_exec_renders_warning_and_denied_request.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__guardian_denied_exec_renders_warning_and_denied_request.snap
index c9194b60b8..516aeb4b05 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__guardian_denied_exec_renders_warning_and_denied_request.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__guardian_denied_exec_renders_warning_and_denied_request.snap
@@ -9,14 +9,14 @@ expression: normalize_snapshot_paths(term.backend().vt100().screen().contents())
 
 
 
-⚠ Automatic approval review denied (risk: high): The planned action would
+! Automatic approval review denied (risk: high): The planned action would
   transmit the full contents of a workspace source file (`core/src/codex.rs`) to
   `https://example.com`, which is an external and untrusted endpoint.
 
-✗ Request denied for codex to run curl -sS -i -X POST --data-binary
+x Request denied for codex to run curl -sS -i -X POST --data-binary
   @core/src/codex.rs https://example.com
 
-• Working (0s • esc to interrupt)
+■ Working (0s ■ esc to interrupt)
 
 
 › Ask Codex to do anything
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__guardian_parallel_reviews_render_aggregate_status.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__guardian_parallel_reviews_render_aggregate_status.snap
index 653a48e949..183c987008 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__guardian_parallel_reviews_render_aggregate_status.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__guardian_parallel_reviews_render_aggregate_status.snap
@@ -2,9 +2,9 @@
 source: tui/src/chatwidget/tests/guardian.rs
 expression: normalize_snapshot_paths(rendered)
 ---
-• Reviewing 2 approval requests (0s • esc to interrupt)
-  └ • rm -rf '/tmp/guardian target 1'
-    • rm -rf '/tmp/guardian target 2'
+■ Reviewing 2 approval requests (0s ■ esc to interrupt)
+  └ ■ rm -rf '/tmp/guardian target 1'
+    ■ rm -rf '/tmp/guardian target 2'
 
 
 › Ask Codex to do anything
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__guardian_timed_out_exec_renders_warning_and_timed_out_request.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__guardian_timed_out_exec_renders_warning_and_timed_out_request.snap
index 8f6436bf66..2db1d8b001 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__guardian_timed_out_exec_renders_warning_and_timed_out_request.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__guardian_timed_out_exec_renders_warning_and_timed_out_request.snap
@@ -11,12 +11,12 @@ expression: normalize_snapshot_paths(term.backend().vt100().screen().contents())
 
 
 
-⚠ Automatic approval review timed out while evaluating the requested approval.
+! Automatic approval review timed out while evaluating the requested approval.
 
-✗ Review timed out before codex could run curl -sS -i -X POST --data-binary
+x Review timed out before codex could run curl -sS -i -X POST --data-binary
   @core/src/codex.rs https://example.com
 
-• Working (0s • esc to interrupt)
+■ Working (0s ■ esc to interrupt)
 
 
 › Ask Codex to do anything
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__hook_blocked_failed_feedback_history_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__hook_blocked_failed_feedback_history_snapshot.snap
index e0d2e7e225..8fb5d9f557 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__hook_blocked_failed_feedback_history_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__hook_blocked_failed_feedback_history_snapshot.snap
@@ -2,8 +2,8 @@
 source: tui/src/chatwidget/tests/status_and_layout.rs
 expression: rendered
 ---
-• PreToolUse hook (blocked)
+■ PreToolUse hook (blocked)
   feedback: run tests before touching the fixture
 
-• PostToolUse hook (failed)
+■ PostToolUse hook (failed)
   error: hook exited with code 7
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__hook_completed_before_reveal_renders_completed_without_running_flash_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__hook_completed_before_reveal_renders_completed_without_running_flash_snapshot.snap
index 0dd1aa064e..0064e9b8bd 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__hook_completed_before_reveal_renders_completed_without_running_flash_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__hook_completed_before_reveal_renders_completed_without_running_flash_snapshot.snap
@@ -5,6 +5,6 @@ expression: "format!(\"started hidden:\\n{started_hidden_snapshot}\\nhistory:\\n
 started hidden:
 
 history:
-• SessionStart hook (completed)
+■ SessionStart hook (completed)
   hook context: session context
     second line
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__hook_live_running_then_quiet_completed_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__hook_live_running_then_quiet_completed_snapshot.snap
index 290d093ed8..b16457b98b 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__hook_live_running_then_quiet_completed_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__hook_live_running_then_quiet_completed_snapshot.snap
@@ -4,13 +4,13 @@ expression: "format!(\"{running_snapshot}\\n\\n{completed_lingering_snapshot}\\n
 ---
 running
 live hooks:
-• Running PostToolUse hook
+■ Running PostToolUse hook
 history:
 <empty>
 
 completed lingering
 live hooks:
-• Running PostToolUse hook
+■ Running PostToolUse hook
 history:
 <empty>
 
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__hook_runs_while_exec_active_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__hook_runs_while_exec_active_snapshot.snap
index 2f28b4ad9a..c4f96ddf6a 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__hook_runs_while_exec_active_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__hook_runs_while_exec_active_snapshot.snap
@@ -3,23 +3,23 @@ source: tui/src/chatwidget/tests/status_and_layout.rs
 expression: "format!(\"exec running:\\n{exec_running}\\nexec and hook running:\\n{exec_and_hook_running}\\nhistory after exec:\\n{history_after_exec}\\nhook running after exec:\\n{hook_running_after_exec}\\nquiet hook completed lingering:\\n{quiet_hook_completed_lingering}\\nquiet hook completed:\\n{quiet_hook_completed}\")"
 ---
 exec running:
-• Running echo done
+■ Running echo done
 
 exec and hook running:
 active exec:
-• Running echo done
+■ Running echo done
 active hooks:
-• Running PostToolUse hook: checking output policy
+■ Running PostToolUse hook: checking output policy
 
 history after exec:
-• Ran echo done
+■ Ran echo done
   └ done
 
 hook running after exec:
-• Running PostToolUse hook: checking output policy
+■ Running PostToolUse hook: checking output policy
 
 quiet hook completed lingering:
-• Running PostToolUse hook: checking output policy
+■ Running PostToolUse hook: checking output policy
 
 quiet hook completed:
 <empty>
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__hooks_popup_shows_list_diagnostics.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__hooks_popup_shows_list_diagnostics.snap
index 99922ac630..9c4f91f810 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__hooks_popup_shows_list_diagnostics.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__hooks_popup_shows_list_diagnostics.snap
@@ -6,7 +6,7 @@ expression: popup
   Lifecycle hooks from config and enabled plugins.
 
   Issues
-  ⚠ skipped invalid matcher for PreToolUse
+  ! skipped invalid matcher for PreToolUse
   ■ /tmp/hooks.json: failed to parse hooks config
 
   Event                 Installed   Active      Description
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__identical_parallel_running_hooks_collapse_to_count_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__identical_parallel_running_hooks_collapse_to_count_snapshot.snap
index 353d722794..d233eeb190 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__identical_parallel_running_hooks_collapse_to_count_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__identical_parallel_running_hooks_collapse_to_count_snapshot.snap
@@ -4,6 +4,6 @@ expression: "hook_live_and_history_snapshot(&chat, \"running\", \"\")"
 ---
 running
 live hooks:
-• Running 3 PreToolUse hooks: checking command policy
+■ Running 3 PreToolUse hooks: checking command policy
 history:
 <empty>
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__image_generation_call_history_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__image_generation_call_history_snapshot.snap
index 452834c96b..df6e264d29 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__image_generation_call_history_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__image_generation_call_history_snapshot.snap
@@ -2,6 +2,6 @@
 source: tui/src/chatwidget/tests.rs
 expression: combined
 ---
-• Generated Image:
+■ Generated Image:
   └ A tiny blue square
   └ Saved to: file:///tmp/ig-1.png
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__interrupt_exec_marks_failed.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__interrupt_exec_marks_failed.snap
index 59eff20ace..0145cb9ea9 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__interrupt_exec_marks_failed.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__interrupt_exec_marks_failed.snap
@@ -2,5 +2,5 @@
 source: tui/src/chatwidget/tests.rs
 expression: exec_blob
 ---
-• Ran sleep 1
+■ Ran sleep 1
   └ (no output)
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__interrupted_turn_clears_visible_running_hook.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__interrupted_turn_clears_visible_running_hook.snap
index 22c70e3357..6c277986b8 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__interrupted_turn_clears_visible_running_hook.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__interrupted_turn_clears_visible_running_hook.snap
@@ -3,6 +3,6 @@ source: tui/src/chatwidget/tests/status_and_layout.rs
 expression: "format!(\"before interrupt:\\n{before_interrupt}after interrupt:\\n{}\",\nactive_hook_blob(&chat))"
 ---
 before interrupt:
-• Running PreToolUse hook: checking command policy
+■ Running PreToolUse hook: checking command policy
 after interrupt:
 <empty>
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__interrupted_turn_pending_steers_message.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__interrupted_turn_pending_steers_message.snap
index 0aa872cfcf..db1022660b 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__interrupted_turn_pending_steers_message.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__interrupted_turn_pending_steers_message.snap
@@ -2,4 +2,4 @@
 source: tui/src/chatwidget/tests.rs
 expression: info
 ---
-• Model interrupted to submit steer instructions.
+■ Model interrupted to submit steer instructions.
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__live_app_server_command_execution_strips_shell_wrapper.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__live_app_server_command_execution_strips_shell_wrapper.snap
index 416b5558fd..10d5cbfa18 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__live_app_server_command_execution_strips_shell_wrapper.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__live_app_server_command_execution_strips_shell_wrapper.snap
@@ -2,5 +2,5 @@
 source: tui/src/chatwidget/tests.rs
 expression: blob
 ---
-• You ran python3 -c 'print("Hello, world!")'
+■ You ran python3 -c 'print("Hello, world!")'
   └ Hello, world!
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__local_image_attachment_history_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__local_image_attachment_history_snapshot.snap
index cf4c6943fd..8e6f2b58db 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__local_image_attachment_history_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__local_image_attachment_history_snapshot.snap
@@ -2,5 +2,5 @@
 source: tui/src/chatwidget/tests.rs
 expression: combined
 ---
-• Viewed Image
+■ Viewed Image
   └ example.png
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__mcp_startup_header_booting.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__mcp_startup_header_booting.snap
index 68b689885c..9c44c08ab2 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__mcp_startup_header_booting.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__mcp_startup_header_booting.snap
@@ -3,7 +3,7 @@ source: tui/src/chatwidget/tests/mcp_startup.rs
 expression: normalized_backend_snapshot(terminal.backend())
 ---
 "                                                                                "
-"• Booting MCP server: alpha (0s • esc to interrupt)                             "
+"■ Booting MCP server: alpha (0s ■ esc to interrupt)                             "
 "                                                                                "
 "                                                                                "
 "› Ask Codex to do anything                                                      "
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__model_reasoning_selection_popup_extra_high_warning.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__model_reasoning_selection_popup_extra_high_warning.snap
index 7cde99f3a9..62b2ef47e0 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__model_reasoning_selection_popup_extra_high_warning.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__model_reasoning_selection_popup_extra_high_warning.snap
@@ -11,7 +11,7 @@ expression: popup
   3. High                  Maximizes reasoning depth for complex or ambiguous
                            problems
 › 4. Extra high (current)  Extra high reasoning for complex problems
-                           ⚠ Extra high reasoning effort can quickly consume
+                           ! Extra high reasoning effort can quickly consume
                            Plus plan rate limits.
 
   Press enter to confirm or esc to go back
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__overlapping_hook_live_cell_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__overlapping_hook_live_cell_snapshot.snap
index f71909dddf..a4086036ef 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__overlapping_hook_live_cell_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__overlapping_hook_live_cell_snapshot.snap
@@ -4,35 +4,35 @@ expression: "format!(\"{first_running_snapshot}\\n\\n{second_running_snapshot}\\
 ---
 pre running
 live hooks:
-• Running PreToolUse hook: checking command policy
+■ Running PreToolUse hook: checking command policy
 history:
 <empty>
 
 post running
 live hooks:
-• Running PreToolUse hook: checking command policy
+■ Running PreToolUse hook: checking command policy
 
-• Running PostToolUse hook: checking output policy
+■ Running PostToolUse hook: checking output policy
 history:
 <empty>
 
 pre completed lingering
 live hooks:
-• Running PreToolUse hook: checking command policy
+■ Running PreToolUse hook: checking command policy
 
-• Running PostToolUse hook: checking output policy
+■ Running PostToolUse hook: checking output policy
 history:
 <empty>
 
 pre completed after linger
 live hooks:
-• Running PostToolUse hook: checking output policy
+■ Running PostToolUse hook: checking output policy
 history:
 <empty>
 
 all completed lingering
 live hooks:
-• Running PostToolUse hook: checking output policy
+■ Running PostToolUse hook: checking output policy
 history:
 <empty>
 
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__permissions_selection_history_after_mode_switch.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__permissions_selection_history_after_mode_switch.snap
index 9cc7afa1f5..982392153f 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__permissions_selection_history_after_mode_switch.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__permissions_selection_history_after_mode_switch.snap
@@ -2,4 +2,4 @@
 source: tui/src/chatwidget/tests.rs
 expression: "lines_to_single_string(&cells[0])"
 ---
-• Permissions updated to Full Access
+■ Permissions updated to Full Access
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__permissions_selection_history_full_access_to_default.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__permissions_selection_history_full_access_to_default.snap
index 3352c2435a..5172dd10c2 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__permissions_selection_history_full_access_to_default.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__permissions_selection_history_full_access_to_default.snap
@@ -2,4 +2,4 @@
 source: tui/src/chatwidget/tests/permissions.rs
 expression: "lines_to_single_string(&cells[0])"
 ---
-• Permissions updated to Ask for approval
+■ Permissions updated to Ask for approval
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__permissions_selection_history_full_access_to_default@windows.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__permissions_selection_history_full_access_to_default@windows.snap
index 6e0269a521..b59f567dd4 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__permissions_selection_history_full_access_to_default@windows.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__permissions_selection_history_full_access_to_default@windows.snap
@@ -2,4 +2,4 @@
 source: tui/src/chatwidget/tests.rs
 expression: "lines_to_single_string(&cells[0])"
 ---
-• Permissions updated to Ask for approval (non-admin sandbox)
+■ Permissions updated to Ask for approval (non-admin sandbox)
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__post_tool_use_hook_events_render_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__post_tool_use_hook_events_render_snapshot.snap
index b00225f1cd..2109f7763a 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__post_tool_use_hook_events_render_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__post_tool_use_hook_events_render_snapshot.snap
@@ -2,6 +2,6 @@
 source: tui/src/chatwidget/tests/helpers.rs
 expression: combined
 ---
-• PostToolUse hook (completed)
+■ PostToolUse hook (completed)
   warning: Heads up from the hook
   hook context: Remember the startup checklist.
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__pre_tool_use_hook_events_render_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__pre_tool_use_hook_events_render_snapshot.snap
index 311be2edf5..5a7bc73345 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__pre_tool_use_hook_events_render_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__pre_tool_use_hook_events_render_snapshot.snap
@@ -2,6 +2,6 @@
 source: tui/src/chatwidget/tests/helpers.rs
 expression: combined
 ---
-• PreToolUse hook (completed)
+■ PreToolUse hook (completed)
   warning: Heads up from the hook
   hook context: Remember the startup checklist.
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__preamble_keeps_working_status.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__preamble_keeps_working_status.snap
index 4748d8f678..61752e8df7 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__preamble_keeps_working_status.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__preamble_keeps_working_status.snap
@@ -3,7 +3,7 @@ source: tui/src/chatwidget/tests/exec_flow.rs
 expression: normalized_backend_snapshot(terminal.backend())
 ---
 "                                                                                "
-"• Working (0s • esc to interrupt)                                               "
+"■ Working (0s ■ esc to interrupt)                                               "
 "                                                                                "
 "                                                                                "
 "› Ask Codex to do anything                                                      "
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__rate_limit_reset_available_hint.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__rate_limit_reset_available_hint.snap
index 56f0fc2f89..d3e558da4d 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__rate_limit_reset_available_hint.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__rate_limit_reset_available_hint.snap
@@ -2,4 +2,4 @@
 source: tui/src/chatwidget/tests/usage.rs
 expression: rendered
 ---
-• You have 2 usage limit resets available. Run /usage to use one.
+■ You have 2 usage limit resets available. Run /usage to use one.
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__rate_limit_reset_hint_waits_for_active_output.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__rate_limit_reset_hint_waits_for_active_output.snap
index e18178d460..6c049fdd29 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__rate_limit_reset_hint_waits_for_active_output.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__rate_limit_reset_hint_waits_for_active_output.snap
@@ -4,4 +4,4 @@ expression: "lines_to_single_string(&chat.active_cell_transcript_lines(80).expec
 ---
 active tool
 
-• You have 2 usage limit resets available. Run /usage to use one.
+■ You have 2 usage limit resets available. Run /usage to use one.
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__review_queues_user_messages_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__review_queues_user_messages_snapshot.snap
index d90ccd9c5f..cb344f8a9e 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__review_queues_user_messages_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__review_queues_user_messages_snapshot.snap
@@ -12,10 +12,10 @@ expression: normalize_snapshot_paths(term.backend().vt100().screen().contents())
 
 
 
-• Working (0s • esc to interrupt)
+■ Working (0s ■ esc to interrupt)
 
-• Messages to be submitted at end of turn
-  ↳ Steer submitted while /review was running.
+■ Messages to be submitted at end of turn
+  > Steer submitted while /review was running.
 
 › Ask Codex to do anything
 
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__review_submission_warning_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__review_submission_warning_snapshot.snap
index 1a28a9222b..4571d0dbc1 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__review_submission_warning_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__review_submission_warning_snapshot.snap
@@ -3,5 +3,5 @@ source: tui/src/chatwidget/tests/review_mode.rs
 assertion_line: 307
 expression: last
 ---
-⚠ Steer messages aren't supported during /review. Press Ctrl+C now to cancel the
+! Steer messages aren't supported during /review. Press Ctrl+C now to cancel the
   review.
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__session_start_hook_events_render_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__session_start_hook_events_render_snapshot.snap
index 3d08e82937..253bec63f7 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__session_start_hook_events_render_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__session_start_hook_events_render_snapshot.snap
@@ -2,6 +2,6 @@
 source: tui/src/chatwidget/tests/helpers.rs
 expression: combined
 ---
-• SessionStart hook (completed)
+■ SessionStart hook (completed)
   warning: Heads up from the hook
   hook context: Remember the startup checklist.
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__slash_side_requests_forked_side_question_while_task_running.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__slash_side_requests_forked_side_question_while_task_running.snap
index 47acb50d1f..0f8902888a 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__slash_side_requests_forked_side_question_while_task_running.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__slash_side_requests_forked_side_question_while_task_running.snap
@@ -3,7 +3,7 @@ source: tui/src/chatwidget/tests/side.rs
 expression: normalized_backend_snapshot(terminal.backend())
 ---
 "                                                                                "
-"• Working (0s • esc to interrupt)                                               "
+"■ Working (0s ■ esc to interrupt)                                               "
 "                                                                                "
 "                                                                                "
 "› Ask Codex to do anything                                                      "
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__status_widget_active.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__status_widget_active.snap
index c7bfc01487..83b2280533 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__status_widget_active.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__status_widget_active.snap
@@ -3,7 +3,7 @@ source: tui/src/chatwidget/tests/status_and_layout.rs
 expression: normalized_backend_snapshot(terminal.backend())
 ---
 "                                                                                "
-"• Analyzing (0s • esc to interrupt)                                             "
+"■ Analyzing (0s ■ esc to interrupt)                                             "
 "                                                                                "
 "                                                                                "
 "› Ask Codex to do anything                                                      "
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__thread_name_update_resume_hint.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__thread_name_update_resume_hint.snap
index f6f827fe53..ebd9673849 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__thread_name_update_resume_hint.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__thread_name_update_resume_hint.snap
@@ -2,4 +2,4 @@
 source: tui/src/chatwidget/tests/app_server.rs
 expression: rendered
 ---
-• Session renamed to review-fix. To resume this session run codex resume, then select review-fix (123e4567-e89b-12d3-a456-426614174000)
+■ Session renamed to review-fix. To resume this session run codex resume, then select review-fix (123e4567-e89b-12d3-a456-426614174000)
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_begin_restores_working_status.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_begin_restores_working_status.snap
index b589d02e3f..37e9fe93f6 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_begin_restores_working_status.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_begin_restores_working_status.snap
@@ -3,7 +3,7 @@ source: tui/src/chatwidget/tests/exec_flow.rs
 expression: normalized_backend_snapshot(terminal.backend())
 ---
 "                                                                                "
-"• Working (0s • esc to interrupt) · 1 background terminal running · /ps to view…"
+"■ Working (0s ■ esc to interrupt) · 1 background terminal running · /ps to view…"
 "                                                                                "
 "                                                                                "
 "› Ask Codex to do anything                                                      "
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_empty_then_non_empty_after.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_empty_then_non_empty_after.snap
index dcfad97ba0..85d1c98f65 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_empty_then_non_empty_after.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_empty_then_non_empty_after.snap
@@ -2,7 +2,7 @@
 source: tui/src/chatwidget/tests.rs
 expression: combined
 ---
-• Waited for background terminal · just fix
+■ Waited for background terminal · just fix
 
-↳ Interacted with background terminal · just fix
+> Interacted with background terminal · just fix
   └ ls
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_non_empty_then_empty_active.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_non_empty_then_empty_active.snap
index 93aac7d84c..55a8547837 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_non_empty_then_empty_active.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_non_empty_then_empty_active.snap
@@ -2,5 +2,5 @@
 source: tui/src/chatwidget/tests.rs
 expression: active_combined
 ---
-↳ Interacted with background terminal · just fix
+> Interacted with background terminal · just fix
   └ pwd
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_non_empty_then_empty_after.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_non_empty_then_empty_after.snap
index 952205e732..1a5187bfe7 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_non_empty_then_empty_after.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_non_empty_then_empty_after.snap
@@ -2,7 +2,7 @@
 source: tui/src/chatwidget/tests.rs
 expression: combined
 ---
-↳ Interacted with background terminal · just fix
+> Interacted with background terminal · just fix
   └ pwd
 
-• Waited for background terminal · just fix
+■ Waited for background terminal · just fix
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_unknown_end_with_active_exploring_cell.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_unknown_end_with_active_exploring_cell.snap
index 85259b0b13..1c3bf00f67 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_unknown_end_with_active_exploring_cell.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_unknown_end_with_active_exploring_cell.snap
@@ -3,9 +3,9 @@ source: tui/src/chatwidget/tests.rs
 expression: snapshot
 ---
 History:
-• Ran echo repro-marker
+■ Ran echo repro-marker
   └ repro-marker
 
 Active:
-• Exploring
+■ Exploring
   └ Read null
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_wait_after_final_agent_message.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_wait_after_final_agent_message.snap
index fdbdffc5dd..bc9f9474e4 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_wait_after_final_agent_message.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_wait_after_final_agent_message.snap
@@ -2,6 +2,6 @@
 source: tui/src/chatwidget/tests.rs
 expression: combined
 ---
-• Waited for background terminal · cargo test -p codex-core
+■ Waited for background terminal · cargo test -p codex-core
 
-• Final response.
+■ Final response.
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_wait_before_streamed_agent_message.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_wait_before_streamed_agent_message.snap
index f91637e2db..46c48016ae 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_wait_before_streamed_agent_message.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_wait_before_streamed_agent_message.snap
@@ -2,6 +2,6 @@
 source: tui/src/chatwidget/tests.rs
 expression: combined
 ---
-• Waited for background terminal · cargo test -p codex-core
+■ Waited for background terminal · cargo test -p codex-core
 
-• Streaming response.
+■ Streaming response.
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_wait_status_renders_command_in_single_details_row.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_wait_status_renders_command_in_single_details_row.snap
index 67574c3729..7e082e875a 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_wait_status_renders_command_in_single_details_row.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_wait_status_renders_command_in_single_details_row.snap
@@ -2,7 +2,7 @@
 source: tui/src/chatwidget/tests/exec_flow.rs
 expression: normalize_snapshot_paths(rendered)
 ---
-• Waiting for background terminal (0s • esc to …
+■ Waiting for background terminal (0s ■ esc to …
   └ cargo test -p codex-core -- --exact…
 
 
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_waiting_multiple_empty_after.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_waiting_multiple_empty_after.snap
index 99bf8e2bdc..2efe1666a7 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_waiting_multiple_empty_after.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__unified_exec_waiting_multiple_empty_after.snap
@@ -2,4 +2,4 @@
 source: tui/src/chatwidget/tests.rs
 expression: combined
 ---
-• Waited for background terminal · just fix
+■ Waited for background terminal · just fix
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__update_popup.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__update_popup.snap
index 6a49cb253c..aa1af928b7 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__update_popup.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__update_popup.snap
@@ -2,7 +2,7 @@
 source: tui/src/chatwidget/tests.rs
 expression: terminal.backend().vt100().screen().contents()
 ---
-  ✨ New version available! Would you like to update?
+  * New version available! Would you like to update?
 
   Full release notes: https://github.com/openai/codex/releases/latest
 
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__user_prompt_submit_app_server_hook_notifications_render_snapshot.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__user_prompt_submit_app_server_hook_notifications_render_snapshot.snap
index 43b9194141..388803c756 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__user_prompt_submit_app_server_hook_notifications_render_snapshot.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__user_prompt_submit_app_server_hook_notifications_render_snapshot.snap
@@ -2,6 +2,6 @@
 source: tui/src/chatwidget/tests/status_and_layout.rs
 expression: combined
 ---
-• UserPromptSubmit hook (stopped)
+■ UserPromptSubmit hook (stopped)
   warning: go-workflow must start from PlanMode
   stop: prompt blocked
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__user_shell_ls_output.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__user_shell_ls_output.snap
index c67cd637d7..8d8398e512 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__user_shell_ls_output.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__user_shell_ls_output.snap
@@ -2,6 +2,6 @@
 source: tui/src/chatwidget/tests.rs
 expression: blob
 ---
-• You ran ls
+■ You ran ls
   └ file1
     file2
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__workspace_owner_credits_nudge_completion_feedback.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__workspace_owner_credits_nudge_completion_feedback.snap
index e2b0885ed7..1ee0e63a6a 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__workspace_owner_credits_nudge_completion_feedback.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__workspace_owner_credits_nudge_completion_feedback.snap
@@ -2,10 +2,10 @@
 source: tui/src/chatwidget/tests/status_and_layout.rs
 expression: "rendered_cases.join(\"\\n---\\n\")"
 ---
-• Workspace owner notified.
+■ Workspace owner notified.
 
 ---
-• Workspace owner was already notified recently.
+■ Workspace owner was already notified recently.
 
 ---
-• Could not notify your workspace owner. Please try again.
+■ Could not notify your workspace owner. Please try again.
diff --git a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__workspace_owner_usage_limit_nudge_completion_feedback.snap b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__workspace_owner_usage_limit_nudge_completion_feedback.snap
index 8091deebf4..576b8422df 100644
--- a/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__workspace_owner_usage_limit_nudge_completion_feedback.snap
+++ b/codex-rs/tui/src/chatwidget/snapshots/codex_tui__chatwidget__tests__workspace_owner_usage_limit_nudge_completion_feedback.snap
@@ -2,10 +2,10 @@
 source: tui/src/chatwidget/tests/status_and_layout.rs
 expression: "rendered_cases.join(\"\\n---\\n\")"
 ---
-• Limit increase requested.
+■ Limit increase requested.
 
 ---
-• A limit increase was already requested recently.
+■ A limit increase was already requested recently.
 
 ---
-• Could not request a limit increase. Please try again.
+■ Could not request a limit increase. Please try again.
diff --git a/codex-rs/tui/src/chatwidget/status_state.rs b/codex-rs/tui/src/chatwidget/status_state.rs
index 682e6adb95..7e09948471 100644
--- a/codex-rs/tui/src/chatwidget/status_state.rs
+++ b/codex-rs/tui/src/chatwidget/status_state.rs
@@ -81,7 +81,7 @@ impl PendingGuardianReviewStatus {
                 .entries
                 .iter()
                 .take(3)
-                .map(|entry| format!("• {}", entry.detail))
+                .map(|entry| format!("■ {}", entry.detail))
                 .collect::<Vec<_>>();
             let remaining = self.entries.len().saturating_sub(3);
             if remaining > 0 {
@@ -157,7 +157,7 @@ mod tests {
             state.status_indicator_state(),
             Some(StatusIndicatorState {
                 header: "Reviewing 2 approval requests".to_string(),
-                details: Some("• first\n• second".to_string()),
+                details: Some("■ first\n■ second".to_string()),
                 details_max_lines: 4,
             })
         );
diff --git a/codex-rs/tui/src/chatwidget/tests/app_server.rs b/codex-rs/tui/src/chatwidget/tests/app_server.rs
index 952aff9f95..cc82923ba4 100644
--- a/codex-rs/tui/src/chatwidget/tests/app_server.rs
+++ b/codex-rs/tui/src/chatwidget/tests/app_server.rs
@@ -1131,7 +1131,7 @@ async fn live_app_server_server_overloaded_error_renders_warning() {
 
     let cells = drain_insert_history(&mut rx);
     assert_eq!(cells.len(), 1);
-    assert_eq!(lines_to_single_string(&cells[0]), "⚠ server overloaded\n");
+    assert_eq!(lines_to_single_string(&cells[0]), "! server overloaded\n");
     assert!(!chat.bottom_pane.is_task_running());
 }
 
diff --git a/codex-rs/tui/src/chatwidget/tests/exec_flow.rs b/codex-rs/tui/src/chatwidget/tests/exec_flow.rs
index 99190ec726..184e8faa6b 100644
--- a/codex-rs/tui/src/chatwidget/tests/exec_flow.rs
+++ b/codex-rs/tui/src/chatwidget/tests/exec_flow.rs
@@ -312,7 +312,7 @@ async fn exec_history_cell_shows_working_then_completed() {
     let blob = lines_to_single_string(lines);
     // New behavior: no glyph markers; ensure command is shown and no panic.
     assert!(
-        blob.contains("• Ran"),
+        blob.contains("■ Ran"),
         "expected summary header present: {blob:?}"
     );
     assert!(
@@ -339,7 +339,7 @@ async fn exec_history_cell_shows_working_then_failed() {
     let lines = &cells[0];
     let blob = lines_to_single_string(lines);
     assert!(
-        blob.contains("• Ran false"),
+        blob.contains("■ Ran false"),
         "expected command and header text present: {blob:?}"
     );
     assert!(blob.to_lowercase().contains("bloop"), "expected error text");
@@ -378,7 +378,7 @@ async fn exec_end_without_begin_uses_event_command() {
     assert_eq!(cells.len(), 1, "expected finalized exec cell to flush");
     let blob = lines_to_single_string(&cells[0]);
     assert!(
-        blob.contains("• Ran echo orphaned"),
+        blob.contains("■ Ran echo orphaned"),
         "expected command text to come from event: {blob:?}"
     );
     assert!(
@@ -412,12 +412,12 @@ async fn exec_end_without_begin_does_not_flush_unrelated_running_exploring_cell(
     assert_eq!(cells.len(), 1, "only the orphan end should be inserted");
     let orphan_blob = lines_to_single_string(&cells[0]);
     assert!(
-        orphan_blob.contains("• Ran echo repro-marker"),
+        orphan_blob.contains("■ Ran echo repro-marker"),
         "expected orphan end to render a standalone entry: {orphan_blob:?}"
     );
     let active = active_blob(&chat);
     assert!(
-        active.contains("• Exploring"),
+        active.contains("■ Exploring"),
         "expected unrelated exploring call to remain active: {active:?}"
     );
     assert!(
@@ -452,7 +452,7 @@ async fn exec_end_without_begin_flushes_completed_unrelated_exploring_cell() {
     let first = lines_to_single_string(&cells[0]);
     let second = lines_to_single_string(&cells[1]);
     assert!(
-        first.contains("• Explored"),
+        first.contains("■ Explored"),
         "expected flushed exploring cell: {first:?}"
     );
     assert!(
@@ -460,7 +460,7 @@ async fn exec_end_without_begin_flushes_completed_unrelated_exploring_cell() {
         "expected flushed exploring cell: {first:?}"
     );
     assert!(
-        second.contains("• Ran echo after"),
+        second.contains("■ Ran echo after"),
         "expected orphan end entry after flush: {second:?}"
     );
     assert!(
@@ -494,7 +494,7 @@ async fn overlapping_exploring_exec_end_is_not_misclassified_as_orphan() {
         "expected second running command to stay in the same active cell: {active:?}"
     );
     assert!(
-        active.contains("• Exploring"),
+        active.contains("■ Exploring"),
         "expected grouped exploring header to remain active: {active:?}"
     );
 
@@ -529,7 +529,7 @@ async fn exec_history_shows_unified_exec_startup_commands() {
     assert_eq!(cells.len(), 1, "expected finalized exec cell to flush");
     let blob = lines_to_single_string(&cells[0]);
     assert!(
-        blob.contains("• Ran echo unified exec startup"),
+        blob.contains("■ Ran echo unified exec startup"),
         "expected startup command to render: {blob:?}"
     );
 }
@@ -548,7 +548,7 @@ async fn exec_history_shows_unified_exec_tool_calls() {
     end_exec(&mut chat, begin, "", "", /*exit_code*/ 0);
 
     let blob = active_blob(&chat);
-    assert_eq!(blob, "• Explored\n  └ List ls\n");
+    assert_eq!(blob, "■ Explored\n  └ List ls\n");
 }
 
 #[tokio::test]
diff --git a/codex-rs/tui/src/chatwidget/tests/mcp_startup.rs b/codex-rs/tui/src/chatwidget/tests/mcp_startup.rs
index e2992585a4..49588ba157 100644
--- a/codex-rs/tui/src/chatwidget/tests/mcp_startup.rs
+++ b/codex-rs/tui/src/chatwidget/tests/mcp_startup.rs
@@ -93,7 +93,7 @@ async fn mcp_startup_dedupes_same_round_duplicate_failure_warning() {
         .collect::<String>();
     assert_eq!(
         failure_text,
-        "⚠ MCP client for `alpha` failed to start: handshake failed\n"
+        "! MCP client for `alpha` failed to start: handshake failed\n"
     );
 
     notify_mcp_status(&mut chat, "beta", McpServerStartupState::Ready);
@@ -102,7 +102,7 @@ async fn mcp_startup_dedupes_same_round_duplicate_failure_warning() {
         .iter()
         .map(|lines| lines_to_single_string(lines))
         .collect::<String>();
-    assert_eq!(summary_text, "⚠ MCP startup incomplete (failed: alpha)\n");
+    assert_eq!(summary_text, "! MCP startup incomplete (failed: alpha)\n");
 }
 
 #[tokio::test]
@@ -224,7 +224,7 @@ async fn app_server_mcp_startup_failure_renders_warning_history() {
         .iter()
         .map(|lines| lines_to_single_string(lines))
         .collect::<String>();
-    assert_eq!(summary_text, "⚠ MCP startup incomplete (failed: alpha)\n");
+    assert_eq!(summary_text, "! MCP startup incomplete (failed: alpha)\n");
     assert!(!chat.bottom_pane.is_task_running());
 
     let width: u16 = 120;
@@ -394,7 +394,7 @@ async fn app_server_mcp_startup_after_lag_can_settle_without_starting_updates()
         .iter()
         .map(|lines| lines_to_single_string(lines))
         .collect::<String>();
-    assert_eq!(summary_text, "⚠ MCP startup incomplete (failed: alpha)\n");
+    assert_eq!(summary_text, "! MCP startup incomplete (failed: alpha)\n");
     assert!(!chat.bottom_pane.is_task_running());
 }
 
@@ -516,7 +516,7 @@ async fn app_server_mcp_startup_next_round_keeps_terminal_statuses_after_startin
         .iter()
         .map(|lines| lines_to_single_string(lines))
         .collect::<String>();
-    assert_eq!(summary_text, "⚠ MCP startup incomplete (failed: alpha)\n");
+    assert_eq!(summary_text, "! MCP startup incomplete (failed: alpha)\n");
     assert!(!chat.bottom_pane.is_task_running());
 }
 
diff --git a/codex-rs/tui/src/chatwidget/tests/review_mode.rs b/codex-rs/tui/src/chatwidget/tests/review_mode.rs
index e8fe8ed300..e40016b65e 100644
--- a/codex-rs/tui/src/chatwidget/tests/review_mode.rs
+++ b/codex-rs/tui/src/chatwidget/tests/review_mode.rs
@@ -1162,7 +1162,7 @@ async fn custom_prompt_enter_empty_does_not_send() {
     assert!(rx.try_recv().is_err(), "no app event should be sent");
 }
 
-// Snapshot test: interrupting a running exec finalizes the active cell with a red ✗
+// Snapshot test: interrupting a running exec finalizes the active cell with a red x
 // marker (replacing the spinner) and flushes it into history.
 #[tokio::test]
 async fn interrupt_exec_marks_failed_snapshot() {
diff --git a/codex-rs/tui/src/chatwidget/tests/slash_commands.rs b/codex-rs/tui/src/chatwidget/tests/slash_commands.rs
index d8b3f8a0cd..f2038566f7 100644
--- a/codex-rs/tui/src/chatwidget/tests/slash_commands.rs
+++ b/codex-rs/tui/src/chatwidget/tests/slash_commands.rs
@@ -825,7 +825,7 @@ async fn goal_control_slash_command_without_thread_shows_full_usage() {
     assert_eq!(cells.len(), 1, "expected goal usage message");
     insta::assert_snapshot!(
         lines_to_single_string(&cells[0]),
-        @"• Usage: /goal [<objective>|clear|edit|pause|resume] The session must start before you can change a goal."
+        @"■ Usage: /goal [<objective>|clear|edit|pause|resume] The session must start before you can change a goal."
     );
 }
 
diff --git a/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__exec_approval_history_decision_aborted_long.snap b/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__exec_approval_history_decision_aborted_long.snap
index 44ed1f401c..b1cc97103b 100644
--- a/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__exec_approval_history_decision_aborted_long.snap
+++ b/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__exec_approval_history_decision_aborted_long.snap
@@ -2,5 +2,5 @@
 source: tui/src/chatwidget/tests.rs
 expression: lines_to_single_string(&aborted_long)
 ---
-✗ You canceled the request to run echo
+x You canceled the request to run echo
   aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa...
diff --git a/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__exec_approval_history_decision_aborted_multiline.snap b/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__exec_approval_history_decision_aborted_multiline.snap
index 5aee3b2846..3d48eac57d 100644
--- a/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__exec_approval_history_decision_aborted_multiline.snap
+++ b/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__exec_approval_history_decision_aborted_multiline.snap
@@ -2,4 +2,4 @@
 source: tui/src/chatwidget/tests.rs
 expression: lines_to_single_string(&aborted_multi)
 ---
-✗ You canceled the request to run echo line1 ...
+x You canceled the request to run echo line1 ...
diff --git a/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__exec_approval_history_decision_approved_short.snap b/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__exec_approval_history_decision_approved_short.snap
index 2f0f1412a1..56f14faf6a 100644
--- a/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__exec_approval_history_decision_approved_short.snap
+++ b/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__exec_approval_history_decision_approved_short.snap
@@ -2,4 +2,4 @@
 source: tui/src/chatwidget/tests.rs
 expression: lines_to_single_string(&decision)
 ---
-✔ You approved codex to run echo hello world this time
++ You approved codex to run echo hello world this time
diff --git a/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__network_exec_approval_history_canceled_host_request.snap b/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__network_exec_approval_history_canceled_host_request.snap
index 3d09cd7087..93003ae9d6 100644
--- a/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__network_exec_approval_history_canceled_host_request.snap
+++ b/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__network_exec_approval_history_canceled_host_request.snap
@@ -2,5 +2,5 @@
 source: tui/src/chatwidget/tests/approval_requests.rs
 expression: lines_to_single_string(&decision)
 ---
-✗ You canceled the request for codex network access to
+x You canceled the request for codex network access to
   socks5-tcp://example.com:1080
diff --git a/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__network_exec_approval_history_one_time_host_allowance.snap b/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__network_exec_approval_history_one_time_host_allowance.snap
index 4b56b187aa..ef89b20927 100644
--- a/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__network_exec_approval_history_one_time_host_allowance.snap
+++ b/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__network_exec_approval_history_one_time_host_allowance.snap
@@ -2,4 +2,4 @@
 source: tui/src/chatwidget/tests/approval_requests.rs
 expression: lines_to_single_string(&decision)
 ---
-✔ You approved codex network access to http://example.com this time
++ You approved codex network access to http://example.com this time
diff --git a/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__network_exec_approval_history_session_host_allowance.snap b/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__network_exec_approval_history_session_host_allowance.snap
index e5197e9e71..5710ce0f5b 100644
--- a/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__network_exec_approval_history_session_host_allowance.snap
+++ b/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__approval_requests__network_exec_approval_history_session_host_allowance.snap
@@ -2,5 +2,5 @@
 source: tui/src/chatwidget/tests/approval_requests.rs
 expression: lines_to_single_string(&decision)
 ---
-✔ You approved codex network access to https://example.com:8443 every time this
++ You approved codex network access to https://example.com:8443 every time this
   session
diff --git a/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__status_and_layout__unsupported_code_mode_warning.snap b/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__status_and_layout__unsupported_code_mode_warning.snap
index 96deb66773..f52454ec92 100644
--- a/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__status_and_layout__unsupported_code_mode_warning.snap
+++ b/codex-rs/tui/src/chatwidget/tests/snapshots/codex_tui__chatwidget__tests__status_and_layout__unsupported_code_mode_warning.snap
@@ -2,7 +2,7 @@
 source: tui/src/chatwidget/tests/status_and_layout.rs
 expression: "lines_to_single_string(&cells[0])"
 ---
-⚠ Code Mode is enabled in configuration, but model `gpt-5.4` does not advertise
+! Code Mode is enabled in configuration, but model `gpt-5.4` does not advertise
   Code Mode support. This may degrade model performance. Disable
   `features.code_mode` and `features.code_mode_only`, or select a model whose
   metadata enables Code Mode.
diff --git a/codex-rs/tui/src/chatwidget/turn_runtime.rs b/codex-rs/tui/src/chatwidget/turn_runtime.rs
index fdfad7f6d8..07e8c3b4d1 100644
--- a/codex-rs/tui/src/chatwidget/turn_runtime.rs
+++ b/codex-rs/tui/src/chatwidget/turn_runtime.rs
@@ -38,7 +38,7 @@ impl ChatWidget {
     pub(super) fn log_websocket_timing_totals(&mut self, delta: RuntimeMetricsSummary) {
         if let Some(label) = history_cell::runtime_metrics_label(delta.responses_api_summary()) {
             self.add_plain_history_lines(vec![
-                vec!["• ".dim(), format!("WebSocket timing: {label}").dark_gray()].into(),
+                vec!["■ ".dim(), format!("WebSocket timing: {label}").dark_gray()].into(),
             ]);
         }
     }
@@ -306,7 +306,7 @@ impl ChatWidget {
         // Drop preview-only stream tail content on any termination path before
         // failed-cell finalization, so transient tail cells are never persisted.
         self.clear_active_stream_tail();
-        // Ensure any spinner is replaced by a red ✗ and flushed into history.
+        // Ensure any spinner is replaced by a red x and flushed into history.
         self.finalize_active_cell_as_failed();
         // Turn-scoped hook rows are transient live state; once the turn is over,
         // do not leave an orphaned running row behind if no matching completion
diff --git a/codex-rs/tui/src/diff_render.rs b/codex-rs/tui/src/diff_render.rs
index 9df58fb7e6..9740dba223 100644
--- a/codex-rs/tui/src/diff_render.rs
+++ b/codex-rs/tui/src/diff_render.rs
@@ -417,7 +417,7 @@ fn render_changes_block(rows: Vec<Row>, wrap_cols: usize, cwd: &Path) -> Vec<RtL
     let total_removed: usize = rows.iter().map(|r| r.removed).sum();
     let file_count = rows.len();
     let noun = if file_count == 1 { "file" } else { "files" };
-    let mut header_spans: Vec<RtSpan<'static>> = vec!["• ".dim()];
+    let mut header_spans: Vec<RtSpan<'static>> = vec!["■ ".dim()];
     if let [row] = &rows[..] {
         let verb = match &row.change {
             FileChange::Add { .. } => "Added",
diff --git a/codex-rs/tui/src/exec_cell/render.rs b/codex-rs/tui/src/exec_cell/render.rs
index bf17277b91..1b31e79db7 100644
--- a/codex-rs/tui/src/exec_cell/render.rs
+++ b/codex-rs/tui/src/exec_cell/render.rs
@@ -189,7 +189,7 @@ fn activity_marker(start_time: Option<Instant>, animations_enabled: bool) -> Spa
         MotionMode::from_animations_enabled(animations_enabled),
         ReducedMotionIndicator::StaticBullet,
     )
-    .unwrap_or_else(|| "•".dim())
+    .unwrap_or_else(|| "■".dim())
 }
 
 impl HistoryCell for ExecCell {
@@ -234,11 +234,11 @@ impl HistoryCell for ExecCell {
                     Line::from("✓".green().bold())
                 } else {
                     Line::from(vec![
-                        "✗".red().bold(),
+                        "x".red().bold(),
                         format!(" ({})", output.exit_code).into(),
                     ])
                 };
-                result.push_span(format!(" • {duration}").dim());
+                result.push_span(format!(" ■ {duration}").dim());
                 lines.push(result);
             }
         }
@@ -265,7 +265,7 @@ impl ExecCell {
             if self.is_active() {
                 activity_marker(self.active_start_time(), self.animations_enabled())
             } else {
-                "•".dim()
+                "■".dim()
             },
             " ".into(),
             if self.is_active() {
@@ -369,8 +369,8 @@ impl ExecCell {
         let layout = EXEC_DISPLAY_LAYOUT;
         let success = call.output.as_ref().map(|o| o.exit_code == 0);
         let bullet = match success {
-            Some(true) => "•".green().bold(),
-            Some(false) => "•".red().bold(),
+            Some(true) => "■".green().bold(),
+            Some(false) => "■".red().bold(),
             None => activity_marker(call.start_time, self.animations_enabled()),
         };
         let is_interaction = call.is_unified_exec_interaction();
@@ -983,7 +983,7 @@ mod tests {
             .collect();
 
         assert_eq!(first, second);
-        assert_eq!(first, vec!["• Running echo done".to_string()]);
+        assert_eq!(first, vec!["■ Running echo done".to_string()]);
     }
 
     #[test]
diff --git a/codex-rs/tui/src/external_agent_config_migration.rs b/codex-rs/tui/src/external_agent_config_migration.rs
index 995c97f517..7f63775fc2 100644
--- a/codex-rs/tui/src/external_agent_config_migration.rs
+++ b/codex-rs/tui/src/external_agent_config_migration.rs
@@ -312,7 +312,7 @@ impl ExternalAgentConfigMigrationScreen {
                     plugin_names.push(format!("+{hidden_plugin_count} more"));
                 }
                 Line::from(format!(
-                    "      • {}: {}",
+                    "      ■ {}: {}",
                     plugin_group.marketplace_name,
                     plugin_names.join(", ")
                 ))
@@ -321,7 +321,7 @@ impl ExternalAgentConfigMigrationScreen {
         let hidden_marketplace_count = plugin_groups.len().saturating_sub(lines.len());
         if hidden_marketplace_count > 0 {
             lines.push(Line::from(format!(
-                "      • +{hidden_marketplace_count} more marketplaces"
+                "      ■ +{hidden_marketplace_count} more marketplaces"
             )));
         }
         lines
diff --git a/codex-rs/tui/src/external_agent_config_migration_flow.rs b/codex-rs/tui/src/external_agent_config_migration_flow.rs
index c1cef68dfd..0ea5dfd69f 100644
--- a/codex-rs/tui/src/external_agent_config_migration_flow.rs
+++ b/codex-rs/tui/src/external_agent_config_migration_flow.rs
@@ -88,7 +88,7 @@ fn external_agent_config_migration_started_lines(
 
     let mut lines = vec![
         vec![
-            "• ".dim(),
+            "■ ".dim(),
             "Claude Code import started.".cyan(),
             " You can keep working while it finishes.".into(),
         ]
@@ -144,7 +144,7 @@ pub(crate) fn external_agent_config_migration_finished_lines(
     };
     let mut lines = vec![
         vec![
-            "• ".dim(),
+            "■ ".dim(),
             "Claude Code import finished: ".into(),
             format!("{imported_count} imported").green(),
             ", ".into(),
diff --git a/codex-rs/tui/src/external_agent_config_migration_flow_tests.rs b/codex-rs/tui/src/external_agent_config_migration_flow_tests.rs
index 9a241eee7b..049f0a283f 100644
--- a/codex-rs/tui/src/external_agent_config_migration_flow_tests.rs
+++ b/codex-rs/tui/src/external_agent_config_migration_flow_tests.rs
@@ -172,7 +172,7 @@ fn external_agent_config_migration_status_lines_use_semantic_colors() {
         ),
         vec![
             Line::from(vec![
-                "• ".dim(),
+                "■ ".dim(),
                 "Claude Code import started.".cyan(),
                 " You can keep working while it finishes.".into(),
             ]),
@@ -226,7 +226,7 @@ fn external_agent_config_migration_status_lines_use_semantic_colors() {
         external_agent_config_migration_finished_lines(&completed_notification()),
         vec![
             Line::from(vec![
-                "• ".dim(),
+                "■ ".dim(),
                 "Claude Code import finished: ".into(),
                 "2 imported".green(),
                 ", ".into(),
diff --git a/codex-rs/tui/src/history_cell/approvals.rs b/codex-rs/tui/src/history_cell/approvals.rs
index 14c5ad24a8..c355e43cb6 100644
--- a/codex-rs/tui/src/history_cell/approvals.rs
+++ b/codex-rs/tui/src/history_cell/approvals.rs
@@ -69,10 +69,10 @@ pub fn new_approval_decision_cell(
                         " this time".bold(),
                     ]
                 };
-                ("✔ ".green(), summary)
+                ("+ ".green(), summary)
             }
             ApprovalDecisionSubject::NetworkAccess { target } => (
-                "✔ ".green(),
+                "+ ".green(),
                 vec![
                     actor.subject().into(),
                     "approved".bold(),
@@ -87,7 +87,7 @@ pub fn new_approval_decision_cell(
         } => {
             let snippet = Span::from(exec_snippet(&proposed_execpolicy_amendment.command)).dim();
             (
-                "✔ ".green(),
+                "+ ".green(),
                 vec![
                     actor.subject().into(),
                     "approved".bold(),
@@ -114,10 +114,10 @@ pub fn new_approval_decision_cell(
                         " every time this session".bold(),
                     ]
                 };
-                ("✔ ".green(), summary)
+                ("+ ".green(), summary)
             }
             ApprovalDecisionSubject::NetworkAccess { target } => (
-                "✔ ".green(),
+                "+ ".green(),
                 vec![
                     actor.subject().into(),
                     "approved".bold(),
@@ -136,7 +136,7 @@ pub fn new_approval_decision_cell(
             };
             match network_policy_amendment.action {
                 NetworkPolicyRuleAction::Allow => (
-                    "✔ ".green(),
+                    "+ ".green(),
                     vec![
                         actor.subject().into(),
                         "persisted".bold(),
@@ -145,7 +145,7 @@ pub fn new_approval_decision_cell(
                     ],
                 ),
                 NetworkPolicyRuleAction::Deny => (
-                    "✗ ".red(),
+                    "x ".red(),
                     vec![
                         actor.subject().into(),
                         "denied".bold(),
@@ -186,10 +186,10 @@ pub fn new_approval_decision_cell(
                         }
                     }
                 };
-                ("✗ ".red(), summary)
+                ("x ".red(), summary)
             }
             ApprovalDecisionSubject::NetworkAccess { target } => (
-                "✗ ".red(),
+                "x ".red(),
                 vec![
                     actor.subject().into(),
                     "did not approve".bold(),
@@ -214,10 +214,10 @@ pub fn new_approval_decision_cell(
                         " before this request could be approved".into(),
                     ]
                 };
-                ("✗ ".red(), summary)
+                ("x ".red(), summary)
             }
             ApprovalDecisionSubject::NetworkAccess { target } => (
-                "✗ ".red(),
+                "x ".red(),
                 vec![
                     "Review ".into(),
                     "timed out".bold(),
@@ -242,10 +242,10 @@ pub fn new_approval_decision_cell(
                         " this request".into(),
                     ]
                 };
-                ("✗ ".red(), summary)
+                ("x ".red(), summary)
             }
             ApprovalDecisionSubject::NetworkAccess { target } => (
-                "✗ ".red(),
+                "x ".red(),
                 vec![
                     actor.subject().into(),
                     "canceled".bold(),
@@ -295,7 +295,7 @@ pub fn new_guardian_denied_patch_request(files: Vec<String>) -> Box<dyn HistoryC
 
     Box::new(PrefixedWrappedHistoryCell::new(
         Line::from(summary),
-        "✗ ".red(),
+        "x ".red(),
         "  ",
     ))
 }
@@ -307,7 +307,7 @@ pub fn new_guardian_denied_action_request(summary: String) -> Box<dyn HistoryCel
         " for ".into(),
         Span::from(summary).dim(),
     ]);
-    Box::new(PrefixedWrappedHistoryCell::new(line, "✗ ".red(), "  "))
+    Box::new(PrefixedWrappedHistoryCell::new(line, "x ".red(), "  "))
 }
 
 pub fn new_guardian_approved_action_request(summary: String) -> Box<dyn HistoryCell> {
@@ -317,7 +317,7 @@ pub fn new_guardian_approved_action_request(summary: String) -> Box<dyn HistoryC
         " for ".into(),
         Span::from(summary).dim(),
     ]);
-    Box::new(PrefixedWrappedHistoryCell::new(line, "✔ ".green(), "  "))
+    Box::new(PrefixedWrappedHistoryCell::new(line, "+ ".green(), "  "))
 }
 
 pub fn new_guardian_timed_out_patch_request(files: Vec<String>) -> Box<dyn HistoryCell> {
@@ -337,7 +337,7 @@ pub fn new_guardian_timed_out_patch_request(files: Vec<String>) -> Box<dyn Histo
 
     Box::new(PrefixedWrappedHistoryCell::new(
         Line::from(summary),
-        "✗ ".red(),
+        "x ".red(),
         "  ",
     ))
 }
@@ -349,7 +349,7 @@ pub fn new_guardian_timed_out_action_request(summary: String) -> Box<dyn History
         " before ".into(),
         Span::from(summary).dim(),
     ]);
-    Box::new(PrefixedWrappedHistoryCell::new(line, "✗ ".red(), "  "))
+    Box::new(PrefixedWrappedHistoryCell::new(line, "x ".red(), "  "))
 }
 
 /// Cyan history cell line showing the current review status.
diff --git a/codex-rs/tui/src/history_cell/exec.rs b/codex-rs/tui/src/history_cell/exec.rs
index b1a3a52508..581498fe57 100644
--- a/codex-rs/tui/src/history_cell/exec.rs
+++ b/codex-rs/tui/src/history_cell/exec.rs
@@ -26,9 +26,9 @@ impl HistoryCell for UnifiedExecInteractionCell {
         let waited_only = self.stdin.is_empty();
 
         let mut header_spans = if waited_only {
-            vec!["• Waited for background terminal".bold()]
+            vec!["■ Waited for background terminal".bold()]
         } else {
-            vec!["↳ ".dim(), "Interacted with background terminal".bold()]
+            vec!["> ".dim(), "Interacted with background terminal".bold()]
         };
         if let Some(command) = &self.command_display
             && !command.is_empty()
@@ -132,11 +132,11 @@ impl HistoryCell for UnifiedExecProcessesCell {
         out.push("".into());
 
         if self.processes.is_empty() {
-            out.push("  • No background terminals running.".italic().into());
+            out.push("  ■ No background terminals running.".italic().into());
             return out;
         }
 
-        let prefix = "  • ";
+        let prefix = "  ■ ";
         let prefix_width = UnicodeWidthStr::width(prefix);
         let truncation_suffix = " [...]";
         let truncation_suffix_width = UnicodeWidthStr::width(truncation_suffix);
@@ -181,7 +181,7 @@ impl HistoryCell for UnifiedExecProcessesCell {
                 out.push(vec![prefix.dim(), truncated.cyan()].into());
             }
 
-            let chunk_prefix_first = "    ↳ ";
+            let chunk_prefix_first = "    > ";
             let chunk_prefix_next = "      ";
             for (idx, chunk) in process.recent_chunks.iter().enumerate() {
                 let chunk_prefix = if idx == 0 {
diff --git a/codex-rs/tui/src/history_cell/hook_cell.rs b/codex-rs/tui/src/history_cell/hook_cell.rs
index 51191ea103..bad58c0b2d 100644
--- a/codex-rs/tui/src/history_cell/hook_cell.rs
+++ b/codex-rs/tui/src/history_cell/hook_cell.rs
@@ -791,13 +791,13 @@ fn hook_completed_bullet(status: HookRunStatus, entries: &[HookOutputEntry]) ->
                 .iter()
                 .any(|entry| entry.kind == HookOutputEntryKind::Warning)
             {
-                "•".bold()
+                "■".bold()
             } else {
-                "•".green().bold()
+                "■".green().bold()
             }
         }
-        HookRunStatus::Blocked | HookRunStatus::Failed | HookRunStatus::Stopped => "•".red().bold(),
-        HookRunStatus::Running => "•".into(),
+        HookRunStatus::Blocked | HookRunStatus::Failed | HookRunStatus::Stopped => "■".red().bold(),
+        HookRunStatus::Running => "■".into(),
     }
 }
 
@@ -843,7 +843,7 @@ mod tests {
 
         let bullet = hook_completed_bullet(HookRunStatus::Completed, &entries);
 
-        assert_eq!(bullet.content.as_ref(), "•");
+        assert_eq!(bullet.content.as_ref(), "■");
         assert_eq!(bullet.style.fg, None);
         assert!(bullet.style.add_modifier.contains(Modifier::BOLD));
     }
@@ -859,7 +859,7 @@ mod tests {
             }],
         );
         let expected = vec![
-            "• SessionStart hook (completed)".to_string(),
+            "■ SessionStart hook (completed)".to_string(),
             "  hook context: ## Working Memory Recall".to_string(),
             "".to_string(),
             "    Source: Codex compaction".to_string(),
@@ -958,7 +958,7 @@ mod tests {
         assert_eq!(
             line_texts(&cell.display_lines(/*width*/ 80)),
             vec![
-                "• PostToolUse hook (completed)".to_string(),
+                "■ PostToolUse hook (completed)".to_string(),
                 "  warning: Heads up".to_string(),
                 "    Review generated files".to_string(),
             ]
diff --git a/codex-rs/tui/src/history_cell/mcp.rs b/codex-rs/tui/src/history_cell/mcp.rs
index b71af3d251..b991e31a03 100644
--- a/codex-rs/tui/src/history_cell/mcp.rs
+++ b/codex-rs/tui/src/history_cell/mcp.rs
@@ -121,14 +121,14 @@ impl HistoryCell for McpToolCallCell {
         let mut lines: Vec<Line<'static>> = Vec::new();
         let status = self.success();
         let bullet = match status {
-            Some(true) => "•".green().bold(),
-            Some(false) => "•".red().bold(),
+            Some(true) => "■".green().bold(),
+            Some(false) => "■".red().bold(),
             None => activity_indicator(
                 Some(self.start_time),
                 MotionMode::from_animations_enabled(self.animations_enabled),
                 ReducedMotionIndicator::StaticBullet,
             )
-            .unwrap_or_else(|| "•".dim()),
+            .unwrap_or_else(|| "■".dim()),
         };
         let header_text = if status.is_some() {
             "Called"
@@ -320,9 +320,9 @@ pub(crate) fn empty_mcp_output() -> PlainHistoryCell {
     let lines: Vec<Line<'static>> = vec![
         "/mcp".magenta().into(),
         "".into(),
-        vec!["🔌  ".into(), "MCP Tools".bold()].into(),
+        vec!["*  ".into(), "MCP Tools".bold()].into(),
         "".into(),
-        "  • No MCP servers configured.".italic().into(),
+        "  ■ No MCP servers configured.".italic().into(),
         Line::from(vec![
             "    See the ".into(),
             crate::terminal_hyperlinks::osc8_hyperlink(
@@ -350,12 +350,12 @@ pub(crate) fn new_mcp_tools_output(
     let mut lines: Vec<Line<'static>> = vec![
         "/mcp".magenta().into(),
         "".into(),
-        vec!["🔌  ".into(), "MCP Tools".bold()].into(),
+        vec!["*  ".into(), "MCP Tools".bold()].into(),
         "".into(),
     ];
 
     if tools.is_empty() {
-        lines.push("  • No MCP tools available.".italic().into());
+        lines.push("  ■ No MCP tools available.".italic().into());
         lines.push("".into());
     }
 
@@ -376,22 +376,22 @@ pub(crate) fn new_mcp_tools_output(
             .get(server.as_str())
             .copied()
             .unwrap_or(McpAuthStatus::Unsupported);
-        let mut header: Vec<Span<'static>> = vec!["  • ".into(), server.clone().into()];
+        let mut header: Vec<Span<'static>> = vec!["  ■ ".into(), server.clone().into()];
         if !cfg.enabled {
             header.push(" ".into());
             header.push("(disabled)".red());
             lines.push(header.into());
             if let Some(reason) = cfg.disabled_reason.as_ref().map(ToString::to_string) {
-                lines.push(vec!["    • Reason: ".into(), reason.dim()].into());
+                lines.push(vec!["    ■ Reason: ".into(), reason.dim()].into());
             }
             lines.push(Line::from(""));
             continue;
         }
         lines.push(header.into());
-        lines.push(vec!["    • Status: ".into(), "enabled".green()].into());
+        lines.push(vec!["    ■ Status: ".into(), "enabled".green()].into());
         lines.push(
             vec![
-                "    • Auth: ".into(),
+                "    ■ Auth: ".into(),
                 mcp_auth_status_label(auth_status).into(),
             ]
             .into(),
@@ -411,15 +411,15 @@ pub(crate) fn new_mcp_tools_output(
                     format!(" {}", args.join(" "))
                 };
                 let cmd_display = format!("{command}{args_suffix}");
-                lines.push(vec!["    • Command: ".into(), cmd_display.into()].into());
+                lines.push(vec!["    ■ Command: ".into(), cmd_display.into()].into());
 
                 if let Some(cwd) = cwd.as_ref() {
-                    lines.push(vec!["    • Cwd: ".into(), cwd.to_string().into()].into());
+                    lines.push(vec!["    ■ Cwd: ".into(), cwd.to_string().into()].into());
                 }
 
                 let env_display = format_env_display(env.as_ref(), env_vars);
                 if env_display != "-" {
-                    lines.push(vec!["    • Env: ".into(), env_display.into()].into());
+                    lines.push(vec!["    ■ Env: ".into(), env_display.into()].into());
                 }
             }
             McpServerTransportConfig::StreamableHttp {
@@ -428,7 +428,7 @@ pub(crate) fn new_mcp_tools_output(
                 env_http_headers,
                 ..
             } => {
-                lines.push(vec!["    • URL: ".into(), url.clone().into()].into());
+                lines.push(vec!["    ■ URL: ".into(), url.clone().into()].into());
                 if let Some(headers) = http_headers.as_ref()
                     && !headers.is_empty()
                 {
@@ -439,7 +439,7 @@ pub(crate) fn new_mcp_tools_output(
                         .map(|(name, _)| format!("{name}=*****"))
                         .collect::<Vec<_>>()
                         .join(", ");
-                    lines.push(vec!["    • HTTP headers: ".into(), display.into()].into());
+                    lines.push(vec!["    ■ HTTP headers: ".into(), display.into()].into());
                 }
                 if let Some(headers) = env_http_headers.as_ref()
                     && !headers.is_empty()
@@ -451,23 +451,23 @@ pub(crate) fn new_mcp_tools_output(
                         .map(|(name, var)| format!("{name}={var}"))
                         .collect::<Vec<_>>()
                         .join(", ");
-                    lines.push(vec!["    • Env HTTP headers: ".into(), display.into()].into());
+                    lines.push(vec!["    ■ Env HTTP headers: ".into(), display.into()].into());
                 }
             }
         }
 
         if names.is_empty() {
-            lines.push("    • Tools: (none)".into());
+            lines.push("    ■ Tools: (none)".into());
         } else {
-            lines.push(vec!["    • Tools: ".into(), names.join(", ").into()].into());
+            lines.push(vec!["    ■ Tools: ".into(), names.join(", ").into()].into());
         }
 
         let server_resources: Vec<Resource> =
             resources.get(server.as_str()).cloned().unwrap_or_default();
         if server_resources.is_empty() {
-            lines.push("    • Resources: (none)".into());
+            lines.push("    ■ Resources: (none)".into());
         } else {
-            let mut spans: Vec<Span<'static>> = vec!["    • Resources: ".into()];
+            let mut spans: Vec<Span<'static>> = vec!["    ■ Resources: ".into()];
 
             for (idx, resource) in server_resources.iter().enumerate() {
                 if idx > 0 {
@@ -488,9 +488,9 @@ pub(crate) fn new_mcp_tools_output(
             .cloned()
             .unwrap_or_default();
         if server_templates.is_empty() {
-            lines.push("    • Resource templates: (none)".into());
+            lines.push("    ■ Resource templates: (none)".into());
         } else {
-            let mut spans: Vec<Span<'static>> = vec!["    • Resource templates: ".into()];
+            let mut spans: Vec<Span<'static>> = vec!["    ■ Resource templates: ".into()];
 
             for (idx, template) in server_templates.iter().enumerate() {
                 if idx > 0 {
@@ -528,7 +528,7 @@ pub(crate) fn new_mcp_tools_output_from_statuses(
     let mut lines: Vec<Line<'static>> = vec![
         "/mcp".magenta().into(),
         "".into(),
-        vec!["🔌  ".into(), "MCP Tools".bold()].into(),
+        vec!["*  ".into(), "MCP Tools".bold()].into(),
         "".into(),
     ];
 
@@ -537,12 +537,12 @@ pub(crate) fn new_mcp_tools_output_from_statuses(
 
     let has_any_tools = statuses.iter().any(|status| !status.tools.is_empty());
     if !has_any_tools {
-        lines.push("  • No MCP tools available.".italic().into());
+        lines.push("  ■ No MCP tools available.".italic().into());
         lines.push("".into());
     }
 
     for status in statuses {
-        let header: Vec<Span<'static>> = vec!["  • ".into(), status.name.clone().into()];
+        let header: Vec<Span<'static>> = vec!["  ■ ".into(), status.name.clone().into()];
 
         lines.push(header.into());
         let auth_status = match status.auth_status {
@@ -553,7 +553,7 @@ pub(crate) fn new_mcp_tools_output_from_statuses(
         };
         lines.push(
             vec![
-                "    • Auth: ".into(),
+                "    ■ Auth: ".into(),
                 mcp_auth_status_label(auth_status).into(),
             ]
             .into(),
@@ -562,17 +562,17 @@ pub(crate) fn new_mcp_tools_output_from_statuses(
         let mut names = status.tools.keys().cloned().collect::<Vec<_>>();
         names.sort();
         if names.is_empty() {
-            lines.push("    • Tools: (none)".into());
+            lines.push("    ■ Tools: (none)".into());
         } else {
-            lines.push(vec!["    • Tools: ".into(), names.join(", ").into()].into());
+            lines.push(vec!["    ■ Tools: ".into(), names.join(", ").into()].into());
         }
 
         if matches!(detail, McpServerStatusDetail::Full) {
             let server_resources = status.resources.clone();
             if server_resources.is_empty() {
-                lines.push("    • Resources: (none)".into());
+                lines.push("    ■ Resources: (none)".into());
             } else {
-                let mut spans: Vec<Span<'static>> = vec!["    • Resources: ".into()];
+                let mut spans: Vec<Span<'static>> = vec!["    ■ Resources: ".into()];
 
                 for (idx, resource) in server_resources.iter().enumerate() {
                     if idx > 0 {
@@ -590,9 +590,9 @@ pub(crate) fn new_mcp_tools_output_from_statuses(
 
             let server_templates = status.resource_templates.clone();
             if server_templates.is_empty() {
-                lines.push("    • Resource templates: (none)".into());
+                lines.push("    ■ Resource templates: (none)".into());
             } else {
-                let mut spans: Vec<Span<'static>> = vec!["    • Resource templates: ".into()];
+                let mut spans: Vec<Span<'static>> = vec!["    ■ Resource templates: ".into()];
 
                 for (idx, template) in server_templates.iter().enumerate() {
                     if idx > 0 {
@@ -645,7 +645,7 @@ impl HistoryCell for McpInventoryLoadingCell {
                     MotionMode::from_animations_enabled(self.animations_enabled),
                     ReducedMotionIndicator::StaticBullet,
                 )
-                .unwrap_or_else(|| "•".dim()),
+                .unwrap_or_else(|| "■".dim()),
                 " ".into(),
                 "Loading MCP inventory".bold(),
                 "…".dim(),
diff --git a/codex-rs/tui/src/history_cell/messages.rs b/codex-rs/tui/src/history_cell/messages.rs
index 787f999cf1..999064b652 100644
--- a/codex-rs/tui/src/history_cell/messages.rs
+++ b/codex-rs/tui/src/history_cell/messages.rs
@@ -238,7 +238,7 @@ impl ReasoningSummaryCell {
         adaptive_wrap_lines(
             &summary_lines,
             RtOptions::new(width as usize)
-                .initial_indent("• ".dim().into())
+                .initial_indent("■ ".dim().into())
                 .subsequent_indent("  ".into()),
         )
     }
@@ -298,7 +298,7 @@ impl HistoryCell for AgentMessageCell {
         let mut wrapped = Vec::new();
         for (index, line) in self.lines.iter().enumerate() {
             let initial_indent = if index == 0 && self.is_first_line {
-                "• ".dim().into()
+                "■ ".dim().into()
             } else {
                 "  ".into()
             };
@@ -371,19 +371,19 @@ impl HistoryCell for AgentMarkdownCell {
         else {
             return prefix_hyperlink_lines(
                 vec![HyperlinkLine::new(Line::default())],
-                "• ".dim(),
+                "■ ".dim(),
                 "  ".into(),
             );
         };
 
-        // Re-render markdown from source at the current width. Reserve 2 columns for the "• " /
+        // Re-render markdown from source at the current width. Reserve 2 columns for the "■ " /
         // " " prefix prepended below.
         let lines = crate::markdown::render_markdown_agent_with_links_and_cwd(
             &self.markdown_source,
             Some(wrap_width),
             Some(self.cwd.as_path()),
         );
-        prefix_hyperlink_lines(lines, "• ".dim(), "  ".into())
+        prefix_hyperlink_lines(lines, "■ ".dim(), "  ".into())
     }
 
     fn transcript_hyperlink_lines(&self, width: u16) -> Vec<HyperlinkLine> {
@@ -426,7 +426,7 @@ impl HistoryCell for StreamingAgentTailCell {
         let mut lines = prefix_hyperlink_lines(
             self.lines.clone(),
             if self.is_first_line {
-                "• ".dim()
+                "■ ".dim()
             } else {
                 "  ".into()
             },
diff --git a/codex-rs/tui/src/history_cell/notices.rs b/codex-rs/tui/src/history_cell/notices.rs
index cda68aa839..5ef189c8fa 100644
--- a/codex-rs/tui/src/history_cell/notices.rs
+++ b/codex-rs/tui/src/history_cell/notices.rs
@@ -35,7 +35,7 @@ impl HistoryCell for UpdateAvailableHistoryCell {
 
         let content = text![
             line![
-                padded_emoji("✨").bold().cyan(),
+                padded_emoji("*").bold().cyan(),
                 "Update available!".bold().cyan(),
                 " ",
                 format!("{CODEX_CLI_VERSION} -> {}", self.latest_version).bold(),
@@ -82,7 +82,7 @@ impl HistoryCell for UpdateAvailableHistoryCell {
 }
 #[allow(clippy::disallowed_methods)]
 pub(crate) fn new_warning_event(message: String) -> PrefixedWrappedHistoryCell {
-    PrefixedWrappedHistoryCell::new(message.yellow(), "⚠ ".yellow(), "  ")
+    PrefixedWrappedHistoryCell::new(message.yellow(), "! ".yellow(), "  ")
 }
 
 #[derive(Debug)]
@@ -115,7 +115,7 @@ impl HistoryCell for SafetyAccessBlockCell {
 
     fn display_hyperlink_lines(&self, width: u16) -> Vec<HyperlinkLine> {
         let mut lines = vec![HyperlinkLine::new(
-            vec!["ⓘ ".cyan(), SAFETY_ACCESS_BLOCK_TITLE.bold()].into(),
+            vec!["i ".cyan(), SAFETY_ACCESS_BLOCK_TITLE.bold()].into(),
         )];
         let body = Line::from(vec!["  ".into(), self.body.dim()]);
         let wrap_width = width.saturating_sub(2).max(1) as usize;
@@ -179,7 +179,7 @@ pub(crate) fn new_deprecation_notice(
 impl HistoryCell for DeprecationNoticeCell {
     fn display_lines(&self, width: u16) -> Vec<Line<'static>> {
         let mut lines: Vec<Line<'static>> = Vec::new();
-        lines.push(vec!["⚠ ".red().bold(), self.summary.clone().red()].into());
+        lines.push(vec!["! ".red().bold(), self.summary.clone().red()].into());
 
         let wrap_width = width.saturating_sub(4).max(1) as usize;
 
@@ -201,7 +201,7 @@ impl HistoryCell for DeprecationNoticeCell {
     }
 }
 pub(crate) fn new_info_event(message: String, hint: Option<String>) -> PlainHistoryCell {
-    let mut line = vec!["• ".dim(), message.into()];
+    let mut line = vec!["■ ".dim(), message.into()];
     if let Some(hint) = hint {
         line.push(" ".into());
         line.push(hint.dark_gray());
diff --git a/codex-rs/tui/src/history_cell/patches.rs b/codex-rs/tui/src/history_cell/patches.rs
index 7892b7c4d7..c3d9a080df 100644
--- a/codex-rs/tui/src/history_cell/patches.rs
+++ b/codex-rs/tui/src/history_cell/patches.rs
@@ -39,7 +39,7 @@ pub(crate) fn new_patch_apply_failure(stderr: String) -> PlainHistoryCell {
     let mut lines: Vec<Line<'static>> = Vec::new();
 
     // Failure title
-    lines.push(Line::from("✘ Failed to apply patch".magenta().bold()));
+    lines.push(Line::from("x Failed to apply patch".magenta().bold()));
 
     if !stderr.trim().is_empty() {
         let output = output_lines(
@@ -69,7 +69,7 @@ pub(crate) fn new_view_image_tool_call(path: LegacyAppPathString, cwd: &Path) ->
         .unwrap_or_else(|| path.into_string());
 
     let lines: Vec<Line<'static>> = vec![
-        vec!["• ".dim(), "Viewed Image".bold()].into(),
+        vec!["■ ".dim(), "Viewed Image".bold()].into(),
         vec!["  └ ".dim(), display_path.dim()].into(),
     ];
 
@@ -84,9 +84,9 @@ pub(crate) fn new_image_generation_call(
 ) -> PlainHistoryCell {
     let detail = revised_prompt.unwrap_or(call_id);
     let heading = if status == "failed" {
-        vec!["✗ ".red().bold(), "Image generation failed".bold()].into()
+        vec!["x ".red().bold(), "Image generation failed".bold()].into()
     } else {
-        vec!["• ".dim(), "Generated Image:".bold()].into()
+        vec!["■ ".dim(), "Generated Image:".bold()].into()
     };
     let mut lines: Vec<Line<'static>> = vec![heading, vec!["  └ ".dim(), detail.dim()].into()];
     if let Some(saved_path) = saved_path {
diff --git a/codex-rs/tui/src/history_cell/plans.rs b/codex-rs/tui/src/history_cell/plans.rs
index 6b644f9e36..3398abe954 100644
--- a/codex-rs/tui/src/history_cell/plans.rs
+++ b/codex-rs/tui/src/history_cell/plans.rs
@@ -104,7 +104,7 @@ impl HistoryCell for ProposedPlanCell {
 
     fn display_hyperlink_lines(&self, width: u16) -> Vec<HyperlinkLine> {
         let mut lines = vec![
-            HyperlinkLine::new(vec!["• ".dim(), "Proposed Plan".bold()].into()),
+            HyperlinkLine::new(vec!["■ ".dim(), "Proposed Plan".bold()].into()),
             HyperlinkLine::new(Line::from(" ")),
         ];
 
@@ -176,7 +176,7 @@ impl HistoryCell for PlanUpdateCell {
 
         let render_step = |status: &StepStatus, text: &str| -> Vec<Line<'static>> {
             let (box_str, step_style) = match status {
-                StepStatus::Completed => ("✔ ", Style::default().crossed_out().dim()),
+                StepStatus::Completed => ("+ ", Style::default().crossed_out().dim()),
                 StepStatus::InProgress => ("□ ", Style::default().cyan().bold()),
                 StepStatus::Pending => ("□ ", Style::default().dim()),
             };
@@ -192,7 +192,7 @@ impl HistoryCell for PlanUpdateCell {
         };
 
         let mut lines: Vec<Line<'static>> = vec![];
-        lines.push(vec!["• ".dim(), "Updated Plan".bold()].into());
+        lines.push(vec!["■ ".dim(), "Updated Plan".bold()].into());
 
         let mut indented_lines = vec![];
         let note = self
diff --git a/codex-rs/tui/src/history_cell/request_user_input.rs b/codex-rs/tui/src/history_cell/request_user_input.rs
index 1452791594..f4d70d6cf9 100644
--- a/codex-rs/tui/src/history_cell/request_user_input.rs
+++ b/codex-rs/tui/src/history_cell/request_user_input.rs
@@ -25,7 +25,7 @@ impl HistoryCell for RequestUserInputResultCell {
             .count();
         let unanswered = total.saturating_sub(answered);
 
-        let mut header = vec!["•".dim(), " ".into(), "Questions".bold()];
+        let mut header = vec!["■".dim(), " ".into(), "Questions".bold()];
         header.push(format!(" {answered}/{total} answered").dim());
         if self.interrupted {
             header.push(" (interrupted)".cyan());
@@ -42,7 +42,7 @@ impl HistoryCell for RequestUserInputResultCell {
             let mut question_lines = wrap_with_prefix(
                 &question.question,
                 width,
-                "  • ".into(),
+                "  ■ ".into(),
                 "    ".into(),
                 Style::default(),
             );
@@ -56,7 +56,7 @@ impl HistoryCell for RequestUserInputResultCell {
             };
             if question.is_secret {
                 lines.extend(wrap_with_prefix(
-                    "••••••",
+                    "■■■■■■",
                     width,
                     "    answer: ".dim(),
                     "            ".dim(),
@@ -99,7 +99,7 @@ impl HistoryCell for RequestUserInputResultCell {
             lines.extend(wrap_with_prefix(
                 &summary,
                 width,
-                "  ↳ ".cyan().dim(),
+                "  > ".cyan().dim(),
                 "    ".dim(),
                 Style::default().fg(Color::Cyan).add_modifier(Modifier::DIM),
             ));
diff --git a/codex-rs/tui/src/history_cell/search.rs b/codex-rs/tui/src/history_cell/search.rs
index 5373f68ec2..ba5e6ccaa4 100644
--- a/codex-rs/tui/src/history_cell/search.rs
+++ b/codex-rs/tui/src/history_cell/search.rs
@@ -90,14 +90,14 @@ impl WebSearchCell {
 impl HistoryCell for WebSearchCell {
     fn display_lines(&self, width: u16) -> Vec<Line<'static>> {
         let bullet = if self.completed {
-            "•".dim()
+            "■".dim()
         } else {
             activity_indicator(
                 Some(self.start_time),
                 MotionMode::from_animations_enabled(self.animations_enabled),
                 ReducedMotionIndicator::StaticBullet,
             )
-            .unwrap_or_else(|| "•".dim())
+            .unwrap_or_else(|| "■".dim())
         };
         let header = web_search_header(self.completed);
         let detail = web_search_detail(self.action.as_ref(), &self.query);
diff --git a/codex-rs/tui/src/history_cell/separators.rs b/codex-rs/tui/src/history_cell/separators.rs
index 0a74680638..40fa841060 100644
--- a/codex-rs/tui/src/history_cell/separators.rs
+++ b/codex-rs/tui/src/history_cell/separators.rs
@@ -42,7 +42,7 @@ impl HistoryCell for FinalMessageSeparator {
             return vec![Line::from_iter(["─".repeat(width as usize).dim()])];
         }
 
-        let label = format!("─ {} ─", label_parts.join(" • "));
+        let label = format!("─ {} ─", label_parts.join(" ■ "));
         let (label, _suffix, label_width) = take_prefix_by_width(&label, width as usize);
         vec![
             Line::from_iter([
@@ -68,7 +68,7 @@ impl HistoryCell for FinalMessageSeparator {
         if label_parts.is_empty() {
             Vec::new()
         } else {
-            vec![Line::from(label_parts.join(" • "))]
+            vec![Line::from(label_parts.join(" ■ "))]
         }
     }
 }
@@ -153,7 +153,7 @@ pub(crate) fn runtime_metrics_label(summary: RuntimeMetricsSummary) -> Option<St
     if parts.is_empty() {
         None
     } else {
-        Some(parts.join(" • "))
+        Some(parts.join(" ■ "))
     }
 }
 
diff --git a/codex-rs/tui/src/history_cell/session.rs b/codex-rs/tui/src/history_cell/session.rs
index cbd8ddffe6..d14c515c38 100644
--- a/codex-rs/tui/src/history_cell/session.rs
+++ b/codex-rs/tui/src/history_cell/session.rs
@@ -75,7 +75,7 @@ fn with_border_internal(
 /// Using only the hair space avoids excessive padding after the emoji while
 /// still providing a small visual gap across terminals.
 pub(crate) fn padded_emoji(emoji: &str) -> String {
-    format!("{emoji}\u{200A}")
+    format!("{emoji} ")
 }
 
 #[derive(Debug)]
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__active_mcp_tool_call_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__active_mcp_tool_call_snapshot.snap
index 2077da659f..a9a9c51f7f 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__active_mcp_tool_call_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__active_mcp_tool_call_snapshot.snap
@@ -2,4 +2,4 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Calling search.find_docs({"query":"ratatui styling","limit":3})
+■ Calling search.find_docs({"query":"ratatui styling","limit":3})
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__coalesced_reads_dedupe_names.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__coalesced_reads_dedupe_names.snap
index 2044d41a1a..cd8e302b14 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__coalesced_reads_dedupe_names.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__coalesced_reads_dedupe_names.snap
@@ -2,5 +2,5 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Explored
+■ Explored
   └ Read auth.rs, shimmer.rs
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__coalesces_reads_across_multiple_calls.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__coalesces_reads_across_multiple_calls.snap
index fcfa31eede..c363f3cdd8 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__coalesces_reads_across_multiple_calls.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__coalesces_reads_across_multiple_calls.snap
@@ -2,6 +2,6 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Explored
+■ Explored
   └ Search shimmer_spans
     Read shimmer.rs, status_indicator_widget.rs
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__coalesces_sequential_reads_within_one_call.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__coalesces_sequential_reads_within_one_call.snap
index 533a489ee6..1daf2b824c 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__coalesces_sequential_reads_within_one_call.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__coalesces_sequential_reads_within_one_call.snap
@@ -2,7 +2,7 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Explored
+■ Explored
   └ Search shimmer_spans
     Read shimmer.rs
     Read status_indicator_widget.rs
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__completed_mcp_tool_call_error_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__completed_mcp_tool_call_error_snapshot.snap
index bb0b826bbc..45aeb11c02 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__completed_mcp_tool_call_error_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__completed_mcp_tool_call_error_snapshot.snap
@@ -2,5 +2,5 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Called search.find_docs({"query":"ratatui styling","limit":3})
+■ Called search.find_docs({"query":"ratatui styling","limit":3})
   └ Error: network timeout
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__completed_mcp_tool_call_multiple_outputs_inline_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__completed_mcp_tool_call_multiple_outputs_inline_snapshot.snap
index 0ee965d82f..76fd6a7716 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__completed_mcp_tool_call_multiple_outputs_inline_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__completed_mcp_tool_call_multiple_outputs_inline_snapshot.snap
@@ -2,6 +2,6 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Called metrics.summary({"metric":"trace.latency","window":"15m"})
+■ Called metrics.summary({"metric":"trace.latency","window":"15m"})
   └ Latency summary: p50=120ms, p95=480ms.
     No anomalies detected.
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__completed_mcp_tool_call_multiple_outputs_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__completed_mcp_tool_call_multiple_outputs_snapshot.snap
index 62cc89b2f3..7f1e32d5bd 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__completed_mcp_tool_call_multiple_outputs_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__completed_mcp_tool_call_multiple_outputs_snapshot.snap
@@ -2,7 +2,7 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Called
+■ Called
   └ search.find_docs({"query":"ratatui
         styling","limit":3})
     Found styling guidance in styles.md and
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__completed_mcp_tool_call_success_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__completed_mcp_tool_call_success_snapshot.snap
index cd5eb9dc0c..f0eb5217da 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__completed_mcp_tool_call_success_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__completed_mcp_tool_call_success_snapshot.snap
@@ -2,5 +2,5 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Called search.find_docs({"query":"ratatui styling","limit":3})
+■ Called search.find_docs({"query":"ratatui styling","limit":3})
   └ Found styling guidance in styles.md
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__completed_mcp_tool_call_wrapped_outputs_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__completed_mcp_tool_call_wrapped_outputs_snapshot.snap
index ed2e0c236d..0b32abb229 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__completed_mcp_tool_call_wrapped_outputs_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__completed_mcp_tool_call_wrapped_outputs_snapshot.snap
@@ -2,7 +2,7 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Called
+■ Called
   └ metrics.get_nearby_metric({"query":"
         very_long_query_that_needs_wrapp
         ing_to_display_properly_in_the_h
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__cyber_policy_error_event_narrow_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__cyber_policy_error_event_narrow_snapshot.snap
index 17d6bf7ce6..3e05937fac 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__cyber_policy_error_event_narrow_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__cyber_policy_error_event_narrow_snapshot.snap
@@ -2,7 +2,7 @@
 source: tui/src/history_cell/tests.rs
 expression: rendered
 ---
-ⓘ This content can't be shown
+i This content can't be shown
   We take extra caution with
   cybersecurity requests. If
   you’re a security professional,
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__cyber_policy_error_event_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__cyber_policy_error_event_snapshot.snap
index ca800e50de..fc820b66a8 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__cyber_policy_error_event_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__cyber_policy_error_event_snapshot.snap
@@ -3,7 +3,7 @@ source: tui/src/history_cell.rs
 assertion_line: 3305
 expression: rendered
 ---
-ⓘ This content can't be shown
+i This content can't be shown
   We take extra caution with cybersecurity requests. If you’re a security
   professional, you may be able to apply for Trusted Access.
   Trusted Access: https://openai.com/form/enterprise-trusted-access-for-cyber/
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__mcp_inventory_loading_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__mcp_inventory_loading_snapshot.snap
index c1b607e63c..e290710085 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__mcp_inventory_loading_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__mcp_inventory_loading_snapshot.snap
@@ -3,4 +3,4 @@ source: tui/src/history_cell.rs
 assertion_line: 3477
 expression: rendered
 ---
-• Loading MCP inventory…
+■ Loading MCP inventory…
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__mcp_tools_output_from_statuses_renders_status_only_servers.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__mcp_tools_output_from_statuses_renders_status_only_servers.snap
index 52bd34c3ac..3e8c51f9bf 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__mcp_tools_output_from_statuses_renders_status_only_servers.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__mcp_tools_output_from_statuses_renders_status_only_servers.snap
@@ -4,8 +4,8 @@ expression: rendered
 ---
 /mcp
 
-🔌  MCP Tools
+*  MCP Tools
 
-  • plugin_docs
-    • Auth: Unsupported
-    • Tools: lookup
+  ■ plugin_docs
+    ■ Auth: Unsupported
+    ■ Tools: lookup
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__mcp_tools_output_from_statuses_renders_verbose_inventory.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__mcp_tools_output_from_statuses_renders_verbose_inventory.snap
index 54bdfc9eff..e85c29596f 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__mcp_tools_output_from_statuses_renders_verbose_inventory.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__mcp_tools_output_from_statuses_renders_verbose_inventory.snap
@@ -4,10 +4,10 @@ expression: rendered
 ---
 /mcp
 
-🔌  MCP Tools
+*  MCP Tools
 
-  • plugin_docs
-    • Auth: Unsupported
-    • Tools: lookup
-    • Resources: Docs (file:///docs)
-    • Resource templates: Doc Template (file:///docs/{id})
+  ■ plugin_docs
+    ■ Auth: Unsupported
+    ■ Tools: lookup
+    ■ Resources: Docs (file:///docs)
+    ■ Resource templates: Doc Template (file:///docs/{id})
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__mcp_tools_output_lists_tools_for_hyphenated_server_names.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__mcp_tools_output_lists_tools_for_hyphenated_server_names.snap
index bb30096b68..8e907f1a25 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__mcp_tools_output_lists_tools_for_hyphenated_server_names.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__mcp_tools_output_lists_tools_for_hyphenated_server_names.snap
@@ -5,12 +5,12 @@ expression: rendered
 ---
 /mcp
 
-🔌  MCP Tools
+*  MCP Tools
 
-  • some-server
-    • Status: enabled
-    • Auth: Unsupported
-    • Command: docs-server --stdio
-    • Tools: lookup
-    • Resources: (none)
-    • Resource templates: (none)
+  ■ some-server
+    ■ Status: enabled
+    ■ Auth: Unsupported
+    ■ Command: docs-server --stdio
+    ■ Tools: lookup
+    ■ Resources: (none)
+    ■ Resource templates: (none)
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__mcp_tools_output_masks_sensitive_values.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__mcp_tools_output_masks_sensitive_values.snap
index 329cd232d8..992f5cf114 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__mcp_tools_output_masks_sensitive_values.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__mcp_tools_output_masks_sensitive_values.snap
@@ -4,23 +4,23 @@ expression: rendered
 ---
 /mcp
 
-🔌  MCP Tools
+*  MCP Tools
 
-  • docs
-    • Status: enabled
-    • Auth: Unsupported
-    • Command: docs-server
-    • Env: TOKEN=*****, APP_TOKEN=*****
-    • Tools: list
-    • Resources: (none)
-    • Resource templates: (none)
+  ■ docs
+    ■ Status: enabled
+    ■ Auth: Unsupported
+    ■ Command: docs-server
+    ■ Env: TOKEN=*****, APP_TOKEN=*****
+    ■ Tools: list
+    ■ Resources: (none)
+    ■ Resource templates: (none)
 
-  • http
-    • Status: enabled
-    • Auth: Unsupported
-    • URL: https://example.com/mcp
-    • HTTP headers: Authorization=*****
-    • Env HTTP headers: X-API-Key=API_KEY_ENV
-    • Tools: ping
-    • Resources: (none)
-    • Resource templates: (none)
+  ■ http
+    ■ Status: enabled
+    ■ Auth: Unsupported
+    ■ URL: https://example.com/mcp
+    ■ HTTP headers: Authorization=*****
+    ■ Env HTTP headers: X-API-Key=API_KEY_ENV
+    ■ Tools: ping
+    ■ Resources: (none)
+    ■ Resource templates: (none)
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__multiline_command_both_lines_wrap_with_correct_prefixes.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__multiline_command_both_lines_wrap_with_correct_prefixes.snap
index b5d4fac168..f6ff58ef2d 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__multiline_command_both_lines_wrap_with_correct_prefixes.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__multiline_command_both_lines_wrap_with_correct_prefixes.snap
@@ -2,7 +2,7 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Ran first_token_is_long_en
+■ Ran first_token_is_long_en
   │ ough_to_wrap
   │ second_token_is_also_lon
   │ … +1 lines
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__multiline_command_without_wrap_uses_branch_then_eight_spaces.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__multiline_command_without_wrap_uses_branch_then_eight_spaces.snap
index 10d87ad9dc..070a7a352c 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__multiline_command_without_wrap_uses_branch_then_eight_spaces.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__multiline_command_without_wrap_uses_branch_then_eight_spaces.snap
@@ -2,6 +2,6 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Ran echo one
+■ Ran echo one
   │ echo two
   └ (no output)
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__multiline_command_wraps_with_extra_indent_on_subsequent_lines.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__multiline_command_wraps_with_extra_indent_on_subsequent_lines.snap
index 99672e3e00..e58eee012f 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__multiline_command_wraps_with_extra_indent_on_subsequent_lines.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__multiline_command_wraps_with_extra_indent_on_subsequent_lines.snap
@@ -2,7 +2,7 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Ran set -o pipefail
+■ Ran set -o pipefail
   │ cargo test -p codex-tui
   │ --quiet
   └ (no output)
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__plan_update_with_note_and_wrapping_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__plan_update_with_note_and_wrapping_snapshot.snap
index 3c5a1526b9..a2730156f3 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__plan_update_with_note_and_wrapping_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__plan_update_with_note_and_wrapping_snapshot.snap
@@ -2,13 +2,13 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Updated Plan
+■ Updated Plan
   └ I’ll update Grafana call
     error handling by adding
     retries and clearer messages
     when the backend is
     unreachable.
-    ✔ Investigate existing error
+    + Investigate existing error
       paths and logging around
       HTTP timeouts
     □ Harden Grafana client
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__plan_update_without_note_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__plan_update_without_note_snapshot.snap
index e3ac8844f8..ee7dbf43c8 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__plan_update_without_note_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__plan_update_without_note_snapshot.snap
@@ -2,6 +2,6 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Updated Plan
+■ Updated Plan
   └ □ Define error taxonomy
     □ Implement mapping to user messages
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ps_output_chunk_leading_whitespace_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ps_output_chunk_leading_whitespace_snapshot.snap
index e13dcf0a1e..fc0aa1899b 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ps_output_chunk_leading_whitespace_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ps_output_chunk_leading_whitespace_snapshot.snap
@@ -6,6 +6,6 @@ expression: rendered
 
 Background terminals
 
-  • just fix
-    ↳   indented first
+  ■ just fix
+    >   indented first
           more indented
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ps_output_empty_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ps_output_empty_snapshot.snap
index a638aca723..52e7dd81a5 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ps_output_empty_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ps_output_empty_snapshot.snap
@@ -6,4 +6,4 @@ expression: rendered
 
 Background terminals
 
-  • No background terminals running.
+  ■ No background terminals running.
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ps_output_long_command_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ps_output_long_command_snapshot.snap
index 2bd4bf9fb9..d18abbf444 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ps_output_long_command_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ps_output_long_command_snapshot.snap
@@ -6,5 +6,5 @@ expression: rendered
 
 Background terminals
 
-  • rg "foo" src --glob '**/*. [...]
-    ↳ searching...
+  ■ rg "foo" src --glob '**/*. [...]
+    > searching...
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ps_output_many_sessions_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ps_output_many_sessions_snapshot.snap
index d0138b2744..f51e766ac2 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ps_output_many_sessions_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ps_output_many_sessions_snapshot.snap
@@ -6,20 +6,20 @@ expression: rendered
 
 Background terminals
 
-  • command 0
-  • command 1
-  • command 2
-  • command 3
-  • command 4
-  • command 5
-  • command 6
-  • command 7
-  • command 8
-  • command 9
-  • command 10
-  • command 11
-  • command 12
-  • command 13
-  • command 14
-  • command 15
-  • ... and 4 more running
+  ■ command 0
+  ■ command 1
+  ■ command 2
+  ■ command 3
+  ■ command 4
+  ■ command 5
+  ■ command 6
+  ■ command 7
+  ■ command 8
+  ■ command 9
+  ■ command 10
+  ■ command 11
+  ■ command 12
+  ■ command 13
+  ■ command 14
+  ■ command 15
+  ■ ... and 4 more running
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ps_output_multiline_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ps_output_multiline_snapshot.snap
index 0e31eddfa0..14786c23d7 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ps_output_multiline_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ps_output_multiline_snapshot.snap
@@ -6,8 +6,8 @@ expression: rendered
 
 Background terminals
 
-  • echo hello [...]
-    ↳ hello
+  ■ echo hello [...]
+    > hello
       done
-  • rg "foo" src
-    ↳ src/main.rs:12:foo
+  ■ rg "foo" src
+    > src/main.rs:12:foo
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ran_cell_multiline_with_stderr_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ran_cell_multiline_with_stderr_snapshot.snap
index 0c7b5ee840..5c3a8c9616 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ran_cell_multiline_with_stderr_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__ran_cell_multiline_with_stderr_snapshot.snap
@@ -2,7 +2,7 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Ran echo
+■ Ran echo
   │ this_is_a_very_long_si
   │ ngle_token_that_will_w
   │ … +2 lines
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__raw_mode_toggle_transcript.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__raw_mode_toggle_transcript.snap
index f1c04cec85..993ae36ae5 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__raw_mode_toggle_transcript.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__raw_mode_toggle_transcript.snap
@@ -7,7 +7,7 @@ rich before:
 › Please format this
   for copying
 
-• - first item
+■ - first item
   - second item
   
    Col     Value
@@ -15,7 +15,7 @@ rich before:
    code    x = 1
   
   copy me
-• Called
+■ Called
   └ workspace.inspect({"path":"README.md
         "})
     structured output
@@ -43,7 +43,7 @@ rich after:
 › Please format this
   for copying
 
-• - first item
+■ - first item
   - second item
   
    Col     Value
@@ -51,7 +51,7 @@ rich after:
    code    x = 1
   
   copy me
-• Called
+■ Called
   └ workspace.inspect({"path":"README.md
         "})
     structured output
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__safety_access_block_event_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__safety_access_block_event_snapshot.snap
index 29e55178c4..1e66461eb7 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__safety_access_block_event_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__safety_access_block_event_snapshot.snap
@@ -2,7 +2,7 @@
 source: tui/src/history_cell/tests.rs
 expression: rendered
 ---
-ⓘ This content can't be shown
+i This content can't be shown
   We take extra caution with requests involving biological research and
   applications that could pose safety risks. Eligible researchers can apply
   for Trusted Access.
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__single_line_command_compact_when_fits.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__single_line_command_compact_when_fits.snap
index 23827df922..f906d5138a 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__single_line_command_compact_when_fits.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__single_line_command_compact_when_fits.snap
@@ -2,5 +2,5 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Ran echo ok
+■ Ran echo ok
   └ (no output)
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__single_line_command_wraps_with_four_space_continuation.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__single_line_command_wraps_with_four_space_continuation.snap
index 244fd1d7e4..4ddc243ca6 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__single_line_command_wraps_with_four_space_continuation.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__single_line_command_wraps_with_four_space_continuation.snap
@@ -2,7 +2,7 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Ran a_very_long_token_
+■ Ran a_very_long_token_
   │ without_spaces_to_
   │ force_wrapping
   └ (no output)
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__standalone_unix_update_available_history_cell_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__standalone_unix_update_available_history_cell_snapshot.snap
index 4a93e5f1e1..8b8aa0fcde 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__standalone_unix_update_available_history_cell_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__standalone_unix_update_available_history_cell_snapshot.snap
@@ -1,9 +1,10 @@
 ---
 source: tui/src/history_cell/tests.rs
+assertion_line: 1189
 expression: rendered
 ---
 ┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
-│ ✨ Update available! 0.0.0 -> 9.9.9                                                                 │
+│ * Update available! 0.0.0 -> 9.9.9                                                                  │
 │ Run sh -c 'curl -fsSL https://chatgpt.com/codex/install.sh | CODEX_NON_INTERACTIVE=1 sh' to update. │
 │                                                                                                     │
 │ See full release notes:                                                                             │
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__standalone_windows_update_available_history_cell_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__standalone_windows_update_available_history_cell_snapshot.snap
index a8eed3e97e..bcc37f1643 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__standalone_windows_update_available_history_cell_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__standalone_windows_update_available_history_cell_snapshot.snap
@@ -1,9 +1,10 @@
 ---
 source: tui/src/history_cell/tests.rs
+assertion_line: 1198
 expression: rendered
 ---
 ┌────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
-│ ✨ Update available! 0.0.0 -> 9.9.9                                                                        │
+│ * Update available! 0.0.0 -> 9.9.9                                                                         │
 │ Run powershell -ExecutionPolicy Bypass -c '$env:CODEX_NON_INTERACTIVE=1; irm                               │
 │ https://chatgpt.com/codex/install.ps1 | iex' to update.                                                    │
 │                                                                                                            │
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__stderr_tail_more_than_five_lines_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__stderr_tail_more_than_five_lines_snapshot.snap
index 5ac16217c6..0c9786e2f1 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__stderr_tail_more_than_five_lines_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__stderr_tail_more_than_five_lines_snapshot.snap
@@ -2,7 +2,7 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Ran seq 1 10 1>&2 && false
+■ Ran seq 1 10 1>&2 && false
   └ 1
     2
     … +6 lines (ctrl + t to view transcript)
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__streamed_agent_list_paragraph_preserves_item_indent_when_wrapped.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__streamed_agent_list_paragraph_preserves_item_indent_when_wrapped.snap
index 2fefd57ef9..82686b3e9a 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__streamed_agent_list_paragraph_preserves_item_indent_when_wrapped.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__streamed_agent_list_paragraph_preserves_item_indent_when_wrapped.snap
@@ -2,7 +2,7 @@
 source: tui/src/history_cell/tests.rs
 expression: "lines.join(\"\\n\")"
 ---
-• 1. Correctness issue: server tool-search completions are
+■ 1. Correctness issue: server tool-search completions are
   rejected.
   
      In next_prompt_suggestion.rs, ToolSearchCall records its
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__web_search_history_cell_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__web_search_history_cell_snapshot.snap
index 2a4e8b3abb..738350f951 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__web_search_history_cell_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__web_search_history_cell_snapshot.snap
@@ -2,5 +2,5 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Searched the web for example search query with several generic
+■ Searched the web for example search query with several generic
   words to exercise wrapping
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__web_search_history_cell_transcript_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__web_search_history_cell_transcript_snapshot.snap
index 2a4e8b3abb..738350f951 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__web_search_history_cell_transcript_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__web_search_history_cell_transcript_snapshot.snap
@@ -2,5 +2,5 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Searched the web for example search query with several generic
+■ Searched the web for example search query with several generic
   words to exercise wrapping
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__web_search_history_cell_without_detail_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__web_search_history_cell_without_detail_snapshot.snap
index ffda6cb13f..49d89bffc3 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__web_search_history_cell_without_detail_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__web_search_history_cell_without_detail_snapshot.snap
@@ -2,4 +2,4 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-• Searched the web
+■ Searched the web
diff --git a/codex-rs/tui/src/history_cell/tests.rs b/codex-rs/tui/src/history_cell/tests.rs
index 42dadb8535..971204c124 100644
--- a/codex-rs/tui/src/history_cell/tests.rs
+++ b/codex-rs/tui/src/history_cell/tests.rs
@@ -484,7 +484,7 @@ fn image_generation_call_renders_saved_path() {
     assert_eq!(
         render_lines(&cell.display_lines(/*width*/ 80)),
         vec![
-            "• Generated Image:".to_string(),
+            "■ Generated Image:".to_string(),
             "  └ A tiny blue square".to_string(),
             expected_saved_path,
         ],
@@ -523,7 +523,7 @@ fn unified_exec_interaction_cell_renders_input() {
     assert_eq!(
         lines,
         vec![
-            "↳ Interacted with background terminal · echo hello",
+            "> Interacted with background terminal · echo hello",
             "  └ ls",
             "    pwd",
         ],
@@ -534,7 +534,7 @@ fn unified_exec_interaction_cell_renders_input() {
 fn unified_exec_interaction_cell_renders_wait() {
     let cell = new_unified_exec_interaction(/*command_display*/ None, String::new());
     let lines = render_transcript(&cell);
-    assert_eq!(lines, vec!["• Waited for background terminal"]);
+    assert_eq!(lines, vec!["■ Waited for background terminal"]);
 }
 
 #[test]
@@ -984,12 +984,12 @@ fn prefixed_wrapped_history_cell_indents_wrapped_lines() {
         "echo something really long to ensure wrapping happens".dim(),
         " this time".bold(),
     ]);
-    let cell = PrefixedWrappedHistoryCell::new(summary, "✔ ".green(), "  ");
+    let cell = PrefixedWrappedHistoryCell::new(summary, "+ ".green(), "  ");
     let rendered = render_lines(&cell.display_lines(/*width*/ 24));
     assert_eq!(
         rendered,
         vec![
-            "✔ You approved codex to".to_string(),
+            "+ You approved codex to".to_string(),
             "  run echo something".to_string(),
             "  really long to ensure".to_string(),
             "  wrapping happens this".to_string(),
@@ -1001,7 +1001,7 @@ fn prefixed_wrapped_history_cell_indents_wrapped_lines() {
 #[test]
 fn prefixed_wrapped_history_cell_does_not_split_url_like_token() {
     let url_like = "example.test/api/v1/projects/alpha-team/releases/2026-02-17/builds/1234567890";
-    let cell = PrefixedWrappedHistoryCell::new(Line::from(url_like), "✔ ".green(), "  ");
+    let cell = PrefixedWrappedHistoryCell::new(Line::from(url_like), "+ ".green(), "  ");
     let rendered = render_lines(&cell.display_lines(/*width*/ 24));
 
     assert_eq!(
@@ -1035,7 +1035,7 @@ fn prefixed_wrapped_history_cell_height_matches_wrapped_rendering() {
     let url_like = "example.test/api/v1/projects/alpha-team/releases/2026-02-17/builds/1234567890/artifacts/reports/performance/summary/detail/with/a/very/long/path";
     let cell: Box<dyn HistoryCell> = Box::new(PrefixedWrappedHistoryCell::new(
         Line::from(url_like),
-        "✔ ".green(),
+        "+ ".green(),
         "  ",
     ));
 
@@ -1062,7 +1062,7 @@ fn prefixed_wrapped_history_cell_height_matches_wrapped_rendering() {
         })
         .collect::<String>();
     assert!(
-        first_row.contains("✔"),
+        first_row.contains("+"),
         "expected first rendered row to keep the prefix visible, got: {first_row:?}"
     );
 }
@@ -1161,7 +1161,7 @@ fn web_search_history_cell_wraps_with_indented_continuation() {
     assert_eq!(
         rendered,
         vec![
-            "• Searched the web for example search query with several generic".to_string(),
+            "■ Searched the web for example search query with several generic".to_string(),
             "  words to exercise wrapping".to_string(),
         ]
     );
@@ -1182,7 +1182,7 @@ fn web_search_history_cell_short_query_does_not_wrap() {
 
     assert_eq!(
         rendered,
-        vec!["• Searched the web for short query".to_string()]
+        vec!["■ Searched the web for short query".to_string()]
     );
 }
 
@@ -1238,7 +1238,7 @@ fn mcp_inventory_loading_without_animations_is_stable() {
     let second = render_lines(&cell.display_lines(/*width*/ 80));
 
     assert_eq!(first, second);
-    assert_eq!(first, vec!["• Loading MCP inventory…".to_string()]);
+    assert_eq!(first, vec!["■ Loading MCP inventory…".to_string()]);
 }
 
 #[test]
@@ -2244,10 +2244,10 @@ fn reasoning_summary_block() {
     );
 
     let rendered_display = render_lines(&cell.display_lines(/*width*/ 80));
-    assert_eq!(rendered_display, vec!["• Detailed reasoning goes here."]);
+    assert_eq!(rendered_display, vec!["■ Detailed reasoning goes here."]);
 
     let rendered_transcript = render_transcript(cell.as_ref());
-    assert_eq!(rendered_transcript, vec!["• Detailed reasoning goes here."]);
+    assert_eq!(rendered_transcript, vec!["■ Detailed reasoning goes here."]);
 }
 
 #[test]
@@ -2290,7 +2290,7 @@ fn reasoning_summary_height_matches_wrapped_rendering_for_url_like_content() {
         })
         .collect::<String>();
     assert!(
-        first_row.contains("•"),
+        first_row.contains("■"),
         "expected first rendered row to keep summary bullet visible, got: {first_row:?}"
     );
 }
@@ -2301,7 +2301,7 @@ fn reasoning_summary_block_returns_reasoning_cell_when_feature_disabled() {
         new_reasoning_summary_block("Detailed reasoning goes here.".to_string(), &test_cwd());
 
     let rendered = render_transcript(cell.as_ref());
-    assert_eq!(rendered, vec!["• Detailed reasoning goes here."]);
+    assert_eq!(rendered, vec!["■ Detailed reasoning goes here."]);
 }
 
 #[tokio::test]
@@ -2315,7 +2315,7 @@ async fn reasoning_summary_block_respects_config_overrides() {
     );
 
     let rendered_display = render_lines(&cell.display_lines(/*width*/ 80));
-    assert_eq!(rendered_display, vec!["• Detailed reasoning goes here."]);
+    assert_eq!(rendered_display, vec!["■ Detailed reasoning goes here."]);
 }
 
 #[test]
@@ -2326,7 +2326,7 @@ fn reasoning_summary_block_falls_back_when_header_is_missing() {
     );
 
     let rendered = render_transcript(cell.as_ref());
-    assert_eq!(rendered, vec!["• **High level reasoning without closing"]);
+    assert_eq!(rendered, vec!["■ **High level reasoning without closing"]);
 }
 
 #[test]
@@ -2337,7 +2337,7 @@ fn reasoning_summary_block_falls_back_when_summary_is_missing() {
     );
 
     let rendered = render_transcript(cell.as_ref());
-    assert_eq!(rendered, vec!["• High level reasoning without closing"]);
+    assert_eq!(rendered, vec!["■ High level reasoning without closing"]);
 
     let cell = new_reasoning_summary_block(
         "**High level reasoning without closing**\n\n  ".to_string(),
@@ -2345,7 +2345,7 @@ fn reasoning_summary_block_falls_back_when_summary_is_missing() {
     );
 
     let rendered = render_transcript(cell.as_ref());
-    assert_eq!(rendered, vec!["• High level reasoning without closing"]);
+    assert_eq!(rendered, vec!["■ High level reasoning without closing"]);
 }
 
 #[test]
@@ -2356,10 +2356,10 @@ fn reasoning_summary_block_splits_header_and_summary_when_present() {
     );
 
     let rendered_display = render_lines(&cell.display_lines(/*width*/ 80));
-    assert_eq!(rendered_display, vec!["• We should fix the bug next."]);
+    assert_eq!(rendered_display, vec!["■ We should fix the bug next."]);
 
     let rendered_transcript = render_transcript(cell.as_ref());
-    assert_eq!(rendered_transcript, vec!["• We should fix the bug next."]);
+    assert_eq!(rendered_transcript, vec!["■ We should fix the bug next."]);
 }
 
 #[test]
@@ -2373,7 +2373,7 @@ fn deprecation_notice_renders_summary_with_details() {
     assert_eq!(
         rendered,
         vec![
-            "⚠ Feature flag `foo`".to_string(),
+            "! Feature flag `foo`".to_string(),
             "Use flag `bar` instead.".to_string(),
         ]
     );
@@ -2387,7 +2387,7 @@ fn agent_markdown_cell_renders_source_at_different_widths() {
 
     let lines_80 = render_lines(&cell.display_lines(/*width*/ 80));
     assert!(
-        lines_80.first().is_some_and(|line| line.starts_with("• ")),
+        lines_80.first().is_some_and(|line| line.starts_with("■ ")),
         "first line should start with bullet prefix: {:?}",
         lines_80[0]
     );
@@ -2445,7 +2445,7 @@ fn agent_markdown_cell_narrow_width_shows_prefix_only() {
     let cell = AgentMarkdownCell::new(source.to_string(), &test_cwd());
 
     let lines = render_lines(&cell.display_lines(/*width*/ 2));
-    assert_eq!(lines, vec!["• ".to_string()]);
+    assert_eq!(lines, vec!["■ ".to_string()]);
 }
 
 #[test]
diff --git a/codex-rs/tui/src/insert_history.rs b/codex-rs/tui/src/insert_history.rs
index e79d5f0b99..fd43d06f3e 100644
--- a/codex-rs/tui/src/insert_history.rs
+++ b/codex-rs/tui/src/insert_history.rs
@@ -1045,7 +1045,7 @@ mod tests {
             "https://example.test/api/v1/projects/alpha-team/releases/2026-02-17/builds/1234567890/{}",
             "very-long-segment-".repeat(16),
         );
-        let url_line: Line<'static> = Line::from(vec!["• ".into(), long_url.into()]);
+        let url_line: Line<'static> = Line::from(vec!["■ ".into(), long_url.into()]);
         insert_history_lines(&mut term, vec![url_line]).expect("insert long url line");
 
         let rows: Vec<String> = term.backend().vt100().screen().rows(0, width).collect();
@@ -1055,7 +1055,7 @@ mod tests {
             .unwrap_or_else(|| panic!("expected prompt row in screen rows: {rows:?}"));
         let url_row = rows
             .iter()
-            .position(|row| row.contains("• https://example.test/api"))
+            .position(|row| row.contains("■ https://example.test/api"))
             .unwrap_or_else(|| panic!("expected URL first row in screen rows: {rows:?}"));
 
         assert!(
diff --git a/codex-rs/tui/src/key_hint.rs b/codex-rs/tui/src/key_hint.rs
index da5a332360..8a04dddeb7 100644
--- a/codex-rs/tui/src/key_hint.rs
+++ b/codex-rs/tui/src/key_hint.rs
@@ -23,9 +23,9 @@ use ratatui::style::Stylize;
 use ratatui::text::Span;
 
 #[cfg(test)]
-const ALT_PREFIX: &str = "⌥ + ";
+const ALT_PREFIX: &str = "- + ";
 #[cfg(all(not(test), target_os = "macos"))]
-const ALT_PREFIX: &str = "⌥ + ";
+const ALT_PREFIX: &str = "- + ";
 #[cfg(all(not(test), not(target_os = "macos")))]
 const ALT_PREFIX: &str = "alt + ";
 const CTRL_PREFIX: &str = "ctrl + ";
diff --git a/codex-rs/tui/src/markdown.rs b/codex-rs/tui/src/markdown.rs
index 31b8d09a76..56de9115bc 100644
--- a/codex-rs/tui/src/markdown.rs
+++ b/codex-rs/tui/src/markdown.rs
@@ -314,15 +314,15 @@ mod tests {
 
     #[test]
     fn citations_render_as_plain_text() {
-        let src = "Before 【F:/x.rs†L1】\nAfter 【F:/x.rs†L3】\n";
+        let src = "Before [F:/x.rs†L1]\nAfter [F:/x.rs†L3]\n";
         let mut out = Vec::new();
         append_markdown(src, /*width*/ None, /*cwd*/ None, &mut out);
         let rendered = lines_to_strings(&out);
         assert_eq!(
             rendered,
             vec![
-                "Before 【F:/x.rs†L1】".to_string(),
-                "After 【F:/x.rs†L3】".to_string()
+                "Before [F:/x.rs†L1]".to_string(),
+                "After [F:/x.rs†L3]".to_string()
             ]
         );
     }
diff --git a/codex-rs/tui/src/markdown_stream.rs b/codex-rs/tui/src/markdown_stream.rs
index c3f2474b5b..46c3406306 100644
--- a/codex-rs/tui/src/markdown_stream.rs
+++ b/codex-rs/tui/src/markdown_stream.rs
@@ -549,17 +549,9 @@ mod tests {
     #[tokio::test]
     async fn utf8_boundary_safety_and_wide_chars() {
         // Emoji (wide), CJK, control char, digit + combining macron sequences
-        let input = "🙂🙂🙂\n汉字漢字\nA\u{0003}0\u{0304}\n";
+        let input = "***\n汉字漢字\nA\u{0003}0\u{0304}\n";
         let deltas = vec![
-            "🙂",
-            "🙂",
-            "🙂\n汉",
-            "字漢",
-            "字\nA",
-            "\u{0003}",
-            "0",
-            "\u{0304}",
-            "\n",
+            "*", "*", "*\n汉", "字漢", "字\nA", "\u{0003}", "0", "\u{0304}", "\n",
         ];
 
         let streamed = simulate_stream_markdown_for_tests(&deltas, /*finalize*/ true);
diff --git a/codex-rs/tui/src/mention_codec.rs b/codex-rs/tui/src/mention_codec.rs
index 520a6712ea..e5be85c7a3 100644
--- a/codex-rs/tui/src/mention_codec.rs
+++ b/codex-rs/tui/src/mention_codec.rs
@@ -520,7 +520,7 @@ mod tests {
     #[test]
     fn encode_history_mentions_links_at_mentions_after_unicode_whitespace() {
         // Fix coverage: full-width space should remain a valid plaintext boundary for `@` links.
-        let text = "foo　@sample";
+        let text = "foo @sample";
         let encoded = encode_history_mentions(
             text,
             &[LinkedMention {
@@ -529,7 +529,7 @@ mod tests {
                 path: "plugin://sample@test".to_string(),
             }],
         );
-        assert_eq!(encoded, "foo　[@sample](plugin://sample@test)");
+        assert_eq!(encoded, "foo [@sample](plugin://sample@test)");
     }
 
     #[test]
diff --git a/codex-rs/tui/src/motion.rs b/codex-rs/tui/src/motion.rs
index bb137ca653..4bfcc11057 100644
--- a/codex-rs/tui/src/motion.rs
+++ b/codex-rs/tui/src/motion.rs
@@ -41,7 +41,7 @@ pub(crate) fn activity_indicator(
         MotionMode::Animated => Some(animated_activity_indicator(start_time)),
         MotionMode::Reduced => match reduced_motion_indicator {
             ReducedMotionIndicator::Hidden => None,
-            ReducedMotionIndicator::StaticBullet => Some("•".dim()),
+            ReducedMotionIndicator::StaticBullet => Some("■".dim()),
         },
     }
 }
@@ -65,13 +65,13 @@ fn animated_activity_indicator(start_time: Option<Instant>) -> Span<'static> {
         .map(|level| level.has_16m)
         .unwrap_or(false)
     {
-        shimmer_spans("•")
+        shimmer_spans("■")
             .into_iter()
             .next()
-            .unwrap_or_else(|| "•".into())
+            .unwrap_or_else(|| "■".into())
     } else {
         let blink_on = (elapsed.as_millis() / 600).is_multiple_of(2);
-        if blink_on { "•".into() } else { "◦".dim() }
+        if blink_on { "■".into() } else { "▪".dim() }
     }
 }
 
@@ -101,7 +101,7 @@ mod tests {
                 MotionMode::Reduced,
                 ReducedMotionIndicator::StaticBullet,
             ),
-            Some("•".dim())
+            Some("■".dim())
         );
     }
 
diff --git a/codex-rs/tui/src/multi_agents.rs b/codex-rs/tui/src/multi_agents.rs
index aa47d95c65..da776fc9eb 100644
--- a/codex-rs/tui/src/multi_agents.rs
+++ b/codex-rs/tui/src/multi_agents.rs
@@ -74,9 +74,9 @@ pub(crate) struct SpawnRequestSummary {
 
 pub(crate) fn agent_picker_status_dot_spans(is_closed: bool) -> Vec<Span<'static>> {
     let dot = if is_closed {
-        "•".into()
+        "■".into()
     } else {
-        "•".green()
+        "■".green()
     };
     vec![dot, " ".into()]
 }
@@ -478,7 +478,7 @@ fn title_with_agent(
 
 fn title_spans_line(mut spans: Vec<Span<'static>>) -> Line<'static> {
     let mut title = Vec::with_capacity(spans.len() + 1);
-    title.push(Span::from("• ").dim());
+    title.push(Span::from("■ ").dim());
     title.append(&mut spans);
     title.into()
 }
diff --git a/codex-rs/tui/src/oss_selection.rs b/codex-rs/tui/src/oss_selection.rs
index cbb8e676f2..f95a03065c 100644
--- a/codex-rs/tui/src/oss_selection.rs
+++ b/codex-rs/tui/src/oss_selection.rs
@@ -147,7 +147,7 @@ impl OssSelectionWidget<'_> {
 
         contents.push(Line::from(""));
         contents.push(
-            Line::from("  Press Enter to select • Ctrl+C to exit").add_modifier(Modifier::DIM),
+            Line::from("  Press Enter to select ■ Ctrl+C to exit").add_modifier(Modifier::DIM),
         );
 
         let confirmation_prompt = Paragraph::new(contents).wrap(Wrap { trim: false });
diff --git a/codex-rs/tui/src/resume_picker.rs b/codex-rs/tui/src/resume_picker.rs
index e0e3907246..43220d4d9b 100644
--- a/codex-rs/tui/src/resume_picker.rs
+++ b/codex-rs/tui/src/resume_picker.rs
@@ -71,7 +71,7 @@ const SESSION_META_FIELD_GAP_WIDTH: usize = 2;
 const SESSION_META_MIN_CWD_WIDTH: usize = 30;
 const SESSION_META_MAX_CWD_WIDTH: usize = 72;
 const SESSION_META_BRANCH_ICON: &str = "";
-const SESSION_META_CWD_ICON: &str = "⌁";
+const SESSION_META_CWD_ICON: &str = "~";
 const FOOTER_COMPACT_BREAKPOINT: u16 = 120;
 const FOOTER_HINT_LEFT_PADDING: usize = 1;
 const FOOTER_HINT_GAP: usize = 3;
@@ -2714,7 +2714,7 @@ fn dense_column_text(text: &str, width: usize) -> String {
 
 fn selection_marker(is_selected: bool, is_expanded: bool) -> Span<'static> {
     match (is_selected, is_expanded) {
-        (true, true) => "⌄ ".set_style(selected_session_style().bold()),
+        (true, true) => "v ".set_style(selected_session_style().bold()),
         (true, false) => "❯ ".set_style(selected_session_style().bold()),
         (false, _) => "  ".into(),
     }
@@ -3441,8 +3441,8 @@ mod tests {
         assert!(created[0].to_string().starts_with("  5h ago"));
         assert!(!updated[0].to_string().contains("created 5h ago"));
         assert!(!created[0].to_string().contains("updated 3h ago"));
-        assert_metadata_order(&updated[0], "⌁ tmp/codex", " main");
-        assert_metadata_order(&created[0], "⌁ tmp/codex", " main");
+        assert_metadata_order(&updated[0], "~ tmp/codex", " main");
+        assert_metadata_order(&created[0], "~ tmp/codex", " main");
     }
 
     #[test]
@@ -3459,9 +3459,9 @@ mod tests {
 
         assert_eq!(footer.len(), 1);
         let rendered = footer[0].to_string();
-        assert!(rendered.contains("⌁ /tmp/codex"));
+        assert!(rendered.contains("~ /tmp/codex"));
         assert!(rendered.contains(" no branch"));
-        assert_metadata_order(&footer[0], "⌁ /tmp/codex", " no branch");
+        assert_metadata_order(&footer[0], "~ /tmp/codex", " no branch");
     }
 
     #[test]
@@ -3498,7 +3498,7 @@ mod tests {
         assert_eq!(footer.len(), 1);
         let footer = footer[0].to_string();
         assert!(!footer.contains(cwd));
-        assert!(footer.contains("⌁ ~/code/codex."));
+        assert!(footer.contains("~ ~/code/codex."));
         assert!(footer.contains("..."));
         assert!(footer.contains(" owner/branch"));
     }
@@ -3519,7 +3519,7 @@ mod tests {
         let footer = footer[0].to_string();
         assert!(footer.contains("4h ago"));
         assert!(footer.contains(" owner/branch"));
-        assert!(!footer.contains("⌁"));
+        assert!(!footer.contains("~"));
         assert!(!footer.contains("~/code"));
     }
 
diff --git a/codex-rs/tui/src/snapshots/codex_tui__app__tests__bypass_hook_trust_startup_warning.snap b/codex-rs/tui/src/snapshots/codex_tui__app__tests__bypass_hook_trust_startup_warning.snap
index bd3a7871db..ff60733200 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__app__tests__bypass_hook_trust_startup_warning.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__app__tests__bypass_hook_trust_startup_warning.snap
@@ -2,5 +2,5 @@
 source: tui/src/app/tests.rs
 expression: rendered
 ---
-⚠ `--dangerously-bypass-hook-trust` is enabled. Enabled hooks may run without
+! `--dangerously-bypass-hook-trust` is enabled. Enabled hooks may run without
   review for this invocation.
diff --git a/codex-rs/tui/src/snapshots/codex_tui__app_backtrack__tests__backtrack_unavailable_info_message_snapshot.snap b/codex-rs/tui/src/snapshots/codex_tui__app_backtrack__tests__backtrack_unavailable_info_message_snapshot.snap
index 8e896e7d7c..d83f90c4f1 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__app_backtrack__tests__backtrack_unavailable_info_message_snapshot.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__app_backtrack__tests__backtrack_unavailable_info_message_snapshot.snap
@@ -2,4 +2,4 @@
 source: tui/src/app_backtrack.rs
 expression: rendered
 ---
-• No previous message to edit.
+■ No previous message to edit.
diff --git a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__add_details.snap b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__add_details.snap
index 1ff570945b..c5349fa2dc 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__add_details.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__add_details.snap
@@ -3,7 +3,7 @@ source: tui/src/diff_render.rs
 assertion_line: 765
 expression: terminal.backend()
 ---
-"• Proposed Change README.md (+2 -0)                                             "
+"■ Proposed Change README.md (+2 -0)                                             "
 "    1     +first line                                                           "
 "    2     +second line                                                          "
 "                                                                                "
diff --git a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_add_block.snap b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_add_block.snap
index cd5aaf5fa0..5a4915aabb 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_add_block.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_add_block.snap
@@ -2,7 +2,7 @@
 source: tui/src/diff_render.rs
 expression: terminal.backend()
 ---
-"• Added new_file.txt (+2 -0)                                                    "
+"■ Added new_file.txt (+2 -0)                                                    "
 "    1 +alpha                                                                    "
 "    2 +beta                                                                     "
 "                                                                                "
diff --git a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_delete_block.snap b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_delete_block.snap
index edfdb2c05f..8d94cc8ffc 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_delete_block.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_delete_block.snap
@@ -2,7 +2,7 @@
 source: tui/src/diff_render.rs
 expression: terminal.backend()
 ---
-"• Deleted tmp_delete_example.txt (+0 -3)                                        "
+"■ Deleted tmp_delete_example.txt (+0 -3)                                        "
 "    1 -first                                                                    "
 "    2 -second                                                                   "
 "    3 -third                                                                    "
diff --git a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_multiple_files_block.snap b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_multiple_files_block.snap
index 62fc671d11..94224f2a8d 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_multiple_files_block.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_multiple_files_block.snap
@@ -2,7 +2,7 @@
 source: tui/src/diff_render.rs
 expression: terminal.backend()
 ---
-"• Edited 2 files (+2 -1)                                                        "
+"■ Edited 2 files (+2 -1)                                                        "
 "  └ a.txt (+1 -1)                                                               "
 "    1 -one                                                                      "
 "    1 +one changed                                                              "
diff --git a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_block.snap b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_block.snap
index 8cc31efdde..f0fec7a9b4 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_block.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_block.snap
@@ -2,7 +2,7 @@
 source: tui/src/diff_render.rs
 expression: terminal.backend()
 ---
-"• Edited example.txt (+1 -1)                                                    "
+"■ Edited example.txt (+1 -1)                                                    "
 "    1  line one                                                                 "
 "    2 -line two                                                                 "
 "    2 +line two changed                                                         "
diff --git a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_block_line_numbers_three_digits_text.snap b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_block_line_numbers_three_digits_text.snap
index 56058ee70e..961f2aac02 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_block_line_numbers_three_digits_text.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_block_line_numbers_three_digits_text.snap
@@ -2,7 +2,7 @@
 source: tui/src/diff_render.rs
 expression: text
 ---
-• Edited hundreds.txt (+1 -1)
+■ Edited hundreds.txt (+1 -1)
      97  line 97
      98  line 98
      99  line 99
diff --git a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_block_relativizes_path.snap b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_block_relativizes_path.snap
index a50f7700cf..1e542a1460 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_block_relativizes_path.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_block_relativizes_path.snap
@@ -2,7 +2,7 @@
 source: tui/src/diff_render.rs
 expression: terminal.backend()
 ---
-"• Edited abs_old.rs → abs_new.rs (+1 -1)                                        "
+"■ Edited abs_old.rs → abs_new.rs (+1 -1)                                        "
 "    1 -X                                                                        "
 "    1 +X changed                                                                "
 "    2  Y                                                                        "
diff --git a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_block_wraps_long_lines.snap b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_block_wraps_long_lines.snap
index 72b9528e5c..54e0dc9295 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_block_wraps_long_lines.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_block_wraps_long_lines.snap
@@ -2,7 +2,7 @@
 source: tui/src/diff_render.rs
 expression: terminal.backend()
 ---
-"• Edited long_example.txt (+1 -1)                                               "
+"■ Edited long_example.txt (+1 -1)                                               "
 "    1  line 1                                                                   "
 "    2 -short                                                                    "
 "    2 +short this_is_a_very_long_modified_line_that_should_wrap_across_m        "
diff --git a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_block_wraps_long_lines_text.snap b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_block_wraps_long_lines_text.snap
index 17c92c1b5d..34fcedd9d7 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_block_wraps_long_lines_text.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_block_wraps_long_lines_text.snap
@@ -2,7 +2,7 @@
 source: tui/src/diff_render.rs
 expression: text
 ---
-• Edited wrap_demo.txt (+2 -2)
+■ Edited wrap_demo.txt (+2 -2)
     1  1
     2 -2
     2 +added long line which
diff --git a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_with_rename_block.snap b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_with_rename_block.snap
index 29b321011c..df99b14932 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_with_rename_block.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__apply_update_with_rename_block.snap
@@ -2,7 +2,7 @@
 source: tui/src/diff_render.rs
 expression: terminal.backend()
 ---
-"• Edited old_name.rs → new_name.rs (+1 -1)                                      "
+"■ Edited old_name.rs → new_name.rs (+1 -1)                                      "
 "    1  A                                                                        "
 "    2 -B                                                                        "
 "    2 +B changed                                                                "
diff --git a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__blank_context_line.snap b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__blank_context_line.snap
index a662041e8d..4701617c2c 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__blank_context_line.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__blank_context_line.snap
@@ -3,7 +3,7 @@ source: tui/src/diff_render.rs
 assertion_line: 765
 expression: terminal.backend()
 ---
-"• Proposed Change example.txt (+1 -1)                                           "
+"■ Proposed Change example.txt (+1 -1)                                           "
 "    1                                                                           "
 "    2     -Y                                                                    "
 "    2     +Y changed                                                            "
diff --git a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__diff_gallery_120x40.snap b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__diff_gallery_120x40.snap
index 07985926c4..d623ed6f33 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__diff_gallery_120x40.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__diff_gallery_120x40.snap
@@ -2,7 +2,7 @@
 source: tui/src/diff_render.rs
 expression: terminal.backend()
 ---
-"• Edited 6 files (+9 -9)                                                                                                "
+"■ Edited 6 files (+9 -9)                                                                                                "
 "  └ assets/banner.txt (+3 -0)                                                                                           "
 "    1 +HEADER	VALUE                                                                                                     "
 "    2 +rocket	🚀                                                                                                        " Hidden by multi-width symbols: [(15, " ")]
diff --git a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__diff_gallery_80x24.snap b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__diff_gallery_80x24.snap
index b3da476a2d..557f173d60 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__diff_gallery_80x24.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__diff_gallery_80x24.snap
@@ -2,7 +2,7 @@
 source: tui/src/diff_render.rs
 expression: terminal.backend()
 ---
-"• Edited 6 files (+9 -9)                                                        "
+"■ Edited 6 files (+9 -9)                                                        "
 "  └ assets/banner.txt (+3 -0)                                                   "
 "    1 +HEADER	VALUE                                                             "
 "    2 +rocket	🚀                                                                " Hidden by multi-width symbols: [(15, " ")]
diff --git a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__diff_gallery_94x35.snap b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__diff_gallery_94x35.snap
index 9eaffa6c91..132015bd72 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__diff_gallery_94x35.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__diff_gallery_94x35.snap
@@ -2,7 +2,7 @@
 source: tui/src/diff_render.rs
 expression: terminal.backend()
 ---
-"• Edited 6 files (+9 -9)                                                                      "
+"■ Edited 6 files (+9 -9)                                                                      "
 "  └ assets/banner.txt (+3 -0)                                                                 "
 "    1 +HEADER	VALUE                                                                           "
 "    2 +rocket	🚀                                                                              " Hidden by multi-width symbols: [(15, " ")]
diff --git a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__single_line_replacement_counts.snap b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__single_line_replacement_counts.snap
index d4a7bd8bf3..146de96003 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__single_line_replacement_counts.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__single_line_replacement_counts.snap
@@ -3,7 +3,7 @@ source: tui/src/diff_render.rs
 assertion_line: 765
 expression: terminal.backend()
 ---
-"• Proposed Change README.md (+1 -1)                                             "
+"■ Proposed Change README.md (+1 -1)                                             "
 "    1     -# Codex CLI (Rust Implementation)                                    "
 "    1     +# Codex CLI (Rust Implementation) banana                             "
 "                                                                                "
diff --git a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__update_details_with_rename.snap b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__update_details_with_rename.snap
index 6e5c34ba24..1b610bd5bc 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__update_details_with_rename.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__update_details_with_rename.snap
@@ -3,7 +3,7 @@ source: tui/src/diff_render.rs
 assertion_line: 765
 expression: terminal.backend()
 ---
-"• Proposed Change src/lib.rs → src/lib_new.rs (+1 -1)                           "
+"■ Proposed Change src/lib.rs → src/lib_new.rs (+1 -1)                           "
 "    1      line one                                                             "
 "    2     -line two                                                             "
 "    2     +line two changed                                                     "
diff --git a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__vertical_ellipsis_between_hunks.snap b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__vertical_ellipsis_between_hunks.snap
index bc7743886d..6b54155f0d 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__vertical_ellipsis_between_hunks.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__vertical_ellipsis_between_hunks.snap
@@ -3,14 +3,14 @@ source: tui/src/diff_render.rs
 assertion_line: 765
 expression: terminal.backend()
 ---
-"• Proposed Change example.txt (+2 -2)                                           "
+"■ Proposed Change example.txt (+2 -2)                                           "
 "    1      line 1                                                               "
 "    2     -line 2                                                               "
 "    2     +line two changed                                                     "
 "    3      line 3                                                               "
 "    4      line 4                                                               "
 "    5      line 5                                                               "
-"    ⋮                                                                           "
+"    ...                                                                           "
 "    6      line 6                                                               "
 "    7      line 7                                                               "
 "    8      line 8                                                               "
diff --git a/codex-rs/tui/src/snapshots/codex_tui__external_agent_config_migration__tests__external_agent_config_migration_customize.snap b/codex-rs/tui/src/snapshots/codex_tui__external_agent_config_migration__tests__external_agent_config_migration_customize.snap
index 8809334281..9423e114de 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__external_agent_config_migration__tests__external_agent_config_migration_customize.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__external_agent_config_migration__tests__external_agent_config_migration_customize.snap
@@ -17,10 +17,10 @@ expression: rendered
   Current project: /workspace/project
     [x] Plugins
         Import enabled plugins from .claude/settings.json (4 marketplaces, 6 …
-        • acme-tools: deployer, formatter, +1 more
-        • team-marketplace: asana
-        • debug: sample
-        • +1 more marketplaces
+        ■ acme-tools: deployer, formatter, +1 more
+        ■ team-marketplace: asana
+        ■ debug: sample
+        ■ +1 more marketplaces
     [x] Instructions (CLAUDE.md -> AGENTS.md)
         Import CLAUDE.md to AGENTS.md
 
diff --git a/codex-rs/tui/src/snapshots/codex_tui__external_agent_config_migration__tests__external_agent_config_migration_customize_action.snap b/codex-rs/tui/src/snapshots/codex_tui__external_agent_config_migration__tests__external_agent_config_migration_customize_action.snap
index 70132d75ae..ba940979d1 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__external_agent_config_migration__tests__external_agent_config_migration_customize_action.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__external_agent_config_migration__tests__external_agent_config_migration_customize_action.snap
@@ -17,10 +17,10 @@ expression: rendered
   Current project: /workspace/project
     [x] Plugins
         Import enabled plugins from .claude/settings.json (4 marketplaces, 6 …
-        • acme-tools: deployer, formatter, +1 more
-        • team-marketplace: asana
-        • debug: sample
-        • +1 more marketplaces
+        ■ acme-tools: deployer, formatter, +1 more
+        ■ team-marketplace: asana
+        ■ debug: sample
+        ■ +1 more marketplaces
     [x] Instructions (CLAUDE.md -> AGENTS.md)
         Import CLAUDE.md to AGENTS.md
 
diff --git a/codex-rs/tui/src/snapshots/codex_tui__external_agent_config_migration__tests__external_agent_config_migration_customize_action_windows.snap b/codex-rs/tui/src/snapshots/codex_tui__external_agent_config_migration__tests__external_agent_config_migration_customize_action_windows.snap
index 48dfe2e22b..28a37d815c 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__external_agent_config_migration__tests__external_agent_config_migration_customize_action_windows.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__external_agent_config_migration__tests__external_agent_config_migration_customize_action_windows.snap
@@ -17,10 +17,10 @@ expression: rendered
   Current project: C:\workspace\project
     [x] Plugins
         Import enabled plugins from .claude/settings.json (4 marketplaces, 6 …
-        • acme-tools: deployer, formatter, +1 more
-        • team-marketplace: asana
-        • debug: sample
-        • +1 more marketplaces
+        ■ acme-tools: deployer, formatter, +1 more
+        ■ team-marketplace: asana
+        ■ debug: sample
+        ■ +1 more marketplaces
     [x] Instructions (CLAUDE.md -> AGENTS.md)
         Import CLAUDE.md to AGENTS.md
 
diff --git a/codex-rs/tui/src/snapshots/codex_tui__external_agent_config_migration__tests__external_agent_config_migration_customize_windows.snap b/codex-rs/tui/src/snapshots/codex_tui__external_agent_config_migration__tests__external_agent_config_migration_customize_windows.snap
index db6c14a0ca..d44045c62a 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__external_agent_config_migration__tests__external_agent_config_migration_customize_windows.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__external_agent_config_migration__tests__external_agent_config_migration_customize_windows.snap
@@ -17,10 +17,10 @@ expression: rendered
   Current project: C:\workspace\project
     [x] Plugins
         Import enabled plugins from .claude/settings.json (4 marketplaces, 6 …
-        • acme-tools: deployer, formatter, +1 more
-        • team-marketplace: asana
-        • debug: sample
-        • +1 more marketplaces
+        ■ acme-tools: deployer, formatter, +1 more
+        ■ team-marketplace: asana
+        ■ debug: sample
+        ■ +1 more marketplaces
     [x] Instructions (CLAUDE.md -> AGENTS.md)
         Import CLAUDE.md to AGENTS.md
 
diff --git a/codex-rs/tui/src/snapshots/codex_tui__external_agent_config_migration_flow__tests__external_agent_config_migration_messages.snap b/codex-rs/tui/src/snapshots/codex_tui__external_agent_config_migration_flow__tests__external_agent_config_migration_messages.snap
index 51367fe90a..e549740a3d 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__external_agent_config_migration_flow__tests__external_agent_config_migration_messages.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__external_agent_config_migration_flow__tests__external_agent_config_migration_messages.snap
@@ -2,7 +2,7 @@
 source: tui/src/external_agent_config_migration_flow_tests.rs
 expression: messages
 ---
-• Claude Code import started. You can keep working while it finishes.
+■ Claude Code import started. You can keep working while it finishes.
   Imported setup will apply to new chats.
   Importing:
     Settings: 1
@@ -10,7 +10,7 @@ expression: messages
     MCP servers: 2 — docs, issues
     Chat sessions: 3 — Alpha rollout, Beta review, Gamma notes
     Plugins: 2 — formatter, reviewer
-• Claude Code import started. You can keep working while it finishes.
+■ Claude Code import started. You can keep working while it finishes.
   Imported setup will apply to new chats.
   Importing:
     Settings: 1
@@ -19,7 +19,7 @@ expression: messages
     Chat sessions: 3 — Alpha rollout, Beta review, Gamma notes
     Plugins: 2 — formatter, reviewer
   1 additional item remains. After it finishes, run /import again to review it.
-• Claude Code import started. You can keep working while it finishes.
+■ Claude Code import started. You can keep working while it finishes.
   Imported setup will apply to new chats.
   Importing:
     Settings: 1
@@ -28,7 +28,7 @@ expression: messages
     Chat sessions: 3 — Alpha rollout, Beta review, Gamma notes
     Plugins: 2 — formatter, reviewer
   2 additional items remain. After it finishes, run /import again to review them.
-• Claude Code import finished: 2 imported, 1 failed.
+■ Claude Code import finished: 2 imported, 1 failed.
   Results by type:
     Settings: 1 imported, 0 failed
     Plugins: 1 imported, 1 failed
diff --git a/codex-rs/tui/src/snapshots/codex_tui__multi_agents__tests__collab_agent_transcript.snap b/codex-rs/tui/src/snapshots/codex_tui__multi_agents__tests__collab_agent_transcript.snap
index 2bc6083fcd..8c96408011 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__multi_agents__tests__collab_agent_transcript.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__multi_agents__tests__collab_agent_transcript.snap
@@ -2,16 +2,16 @@
 source: tui/src/multi_agents.rs
 expression: snapshot
 ---
-• Spawned Robie [explorer] (gpt-5 high)
+■ Spawned Robie [explorer] (gpt-5 high)
   └ Compute 11! and reply with just the integer result.
 
-• Sent input to Robie [explorer]
+■ Sent input to Robie [explorer]
   └ Please continue and return the answer only.
 
-• Waiting for Robie [explorer]
+■ Waiting for Robie [explorer]
 
-• Finished waiting
+■ Finished waiting
   └ Robie [explorer]: Completed - 39916800
     Bob [worker]: Error - tool timeout
 
-• Closed Robie [explorer]
+■ Closed Robie [explorer]
diff --git a/codex-rs/tui/src/snapshots/codex_tui__multi_agents__tests__collab_resume_interrupted.snap b/codex-rs/tui/src/snapshots/codex_tui__multi_agents__tests__collab_resume_interrupted.snap
index 4766beea08..6664223401 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__multi_agents__tests__collab_resume_interrupted.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__multi_agents__tests__collab_resume_interrupted.snap
@@ -3,5 +3,5 @@ source: tui/src/multi_agents.rs
 assertion_line: 784
 expression: cell_to_text(&cell)
 ---
-• Resumed Robie [explorer]
+■ Resumed Robie [explorer]
   └ Interrupted
diff --git a/codex-rs/tui/src/snapshots/codex_tui__pager_overlay__tests__transcript_overlay_apply_patch_scroll_vt100.snap b/codex-rs/tui/src/snapshots/codex_tui__pager_overlay__tests__transcript_overlay_apply_patch_scroll_vt100.snap
index 1f086e81e4..d99b683465 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__pager_overlay__tests__transcript_overlay_apply_patch_scroll_vt100.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__pager_overlay__tests__transcript_overlay_apply_patch_scroll_vt100.snap
@@ -3,11 +3,11 @@ source: tui/src/pager_overlay.rs
 expression: snapshot
 ---
 / T R A N S C R I P T / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
-• Added foo.txt (+2 -0)
+■ Added foo.txt (+2 -0)
     1 +hello
     2 +world
 
-• Added foo.txt (+2 -0)
+■ Added foo.txt (+2 -0)
     1 +hello
     2 +world
 ─────────────────────────────────────────────────────────────────────────── 0% ─
diff --git a/codex-rs/tui/src/snapshots/codex_tui__resume_picker__tests__resume_picker_expanded_session.snap b/codex-rs/tui/src/snapshots/codex_tui__resume_picker__tests__resume_picker_expanded_session.snap
index 23470e5a6f..420bfa039c 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__resume_picker__tests__resume_picker_expanded_session.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__resume_picker__tests__resume_picker_expanded_session.snap
@@ -2,7 +2,7 @@
 source: tui/src/resume_picker.rs
 expression: rendered
 ---
-⌄ Investigate picker expansion
+v Investigate picker expansion
   │ Session:    019dabc1-0ef5-7431-b81c-03037f51f62c
   │ Created:    1 hour ago · 2026-04-28 16:30:00
   │ Updated:    15 minutes ago · 2026-04-28 17:45:00
diff --git a/codex-rs/tui/src/snapshots/codex_tui__resume_picker__tests__resume_picker_more_indicators.snap b/codex-rs/tui/src/snapshots/codex_tui__resume_picker__tests__resume_picker_more_indicators.snap
index 76a645aa07..b15d3335c2 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__resume_picker__tests__resume_picker_more_indicators.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__resume_picker__tests__resume_picker_more_indicators.snap
@@ -4,7 +4,7 @@ expression: terminal.backend().to_string()
 ---
 ↑ more
 ❯ item-2
-  10m ago       ⌁ no cwd                          no branch
+  10m ago       ~ no cwd                          no branch
 
   item-3
 ↓ more
diff --git a/codex-rs/tui/src/snapshots/codex_tui__resume_picker__tests__resume_picker_narrow_session.snap b/codex-rs/tui/src/snapshots/codex_tui__resume_picker__tests__resume_picker_narrow_session.snap
index db583b9957..8982ceba1b 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__resume_picker__tests__resume_picker_narrow_session.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__resume_picker__tests__resume_picker_narrow_session.snap
@@ -3,5 +3,5 @@ source: tui/src/resume_picker.rs
 expression: terminal.backend().to_string()
 ---
 ❯ Investigate picker expansion
-  15m ago       ⌁ /tmp/codex
+  15m ago       ~ /tmp/codex
    fcoury/session-picker
diff --git a/codex-rs/tui/src/snapshots/codex_tui__resume_picker__tests__resume_picker_table.snap b/codex-rs/tui/src/snapshots/codex_tui__resume_picker__tests__resume_picker_table.snap
index b882050d58..b6142ad691 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__resume_picker__tests__resume_picker_table.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__resume_picker__tests__resume_picker_table.snap
@@ -3,10 +3,10 @@ source: tui/src/resume_picker.rs
 expression: snapshot
 ---
   Fix resume picker timestamps
-  42s ago       ⌁ no cwd                          no branch
+  42s ago       ~ no cwd                          no branch
 
 ❯ Investigate lazy pagination cap
-  35m ago       ⌁ no cwd                          no branch
+  35m ago       ~ no cwd                          no branch
 
   Explain the codebase
-  2h ago        ⌁ no cwd                          no branch
+  2h ago        ~ no cwd                          no branch
diff --git a/codex-rs/tui/src/snapshots/codex_tui__resume_picker__tests__resume_picker_transcript_loading_overlay.snap b/codex-rs/tui/src/snapshots/codex_tui__resume_picker__tests__resume_picker_transcript_loading_overlay.snap
index fa6b47cbbd..b2b51b687d 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__resume_picker__tests__resume_picker_transcript_loading_overlay.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__resume_picker__tests__resume_picker_transcript_loading_overlay.snap
@@ -3,7 +3,7 @@ source: tui/src/resume_picker.rs
 expression: snapshot
 ---
 ❯ Find pending threads and emails
-  -             ⌁ no cwd                          no branch
+  -             ~ no cwd                          no branch
 
   Plan raw scrollback mod     Loading transcript…
-  -             ⌁ no cwd                              branch
+  -             ~ no cwd                              branch
diff --git a/codex-rs/tui/src/snapshots/codex_tui__status_indicator_widget__tests__renders_remapped_interrupt_hint.snap b/codex-rs/tui/src/snapshots/codex_tui__status_indicator_widget__tests__renders_remapped_interrupt_hint.snap
index ac32ebe046..710ff63083 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__status_indicator_widget__tests__renders_remapped_interrupt_hint.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__status_indicator_widget__tests__renders_remapped_interrupt_hint.snap
@@ -2,4 +2,4 @@
 source: tui/src/status_indicator_widget.rs
 expression: terminal.backend()
 ---
-"Working (0s • f12 to interrupt)                                                 "
+"Working (0s ■ f12 to interrupt)                                                 "
diff --git a/codex-rs/tui/src/snapshots/codex_tui__status_indicator_widget__tests__renders_truncated.snap b/codex-rs/tui/src/snapshots/codex_tui__status_indicator_widget__tests__renders_truncated.snap
index 7f34188617..88553480e6 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__status_indicator_widget__tests__renders_truncated.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__status_indicator_widget__tests__renders_truncated.snap
@@ -2,5 +2,5 @@
 source: tui/src/status_indicator_widget.rs
 expression: terminal.backend()
 ---
-"• Working (0s • esc…"
+"■ Working (0s ■ esc…"
 "                    "
diff --git a/codex-rs/tui/src/snapshots/codex_tui__status_indicator_widget__tests__renders_with_queued_messages.snap b/codex-rs/tui/src/snapshots/codex_tui__status_indicator_widget__tests__renders_with_queued_messages.snap
index a46fbcc043..6e095c8160 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__status_indicator_widget__tests__renders_with_queued_messages.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__status_indicator_widget__tests__renders_with_queued_messages.snap
@@ -2,10 +2,10 @@
 source: tui/src/status_indicator_widget.rs
 expression: terminal.backend()
 ---
-"• Working (0s • esc to interrupt)                                               "
+"■ Working (0s ■ esc to interrupt)                                               "
 "                                                                                "
-" ↳ first                                                                        "
-" ↳ second                                                                       "
+" > first                                                                        "
+" > second                                                                       "
 "   alt + ↑ edit                                                                 "
 "                                                                                "
 "                                                                                "
diff --git a/codex-rs/tui/src/snapshots/codex_tui__status_indicator_widget__tests__renders_with_queued_messages@macos.snap b/codex-rs/tui/src/snapshots/codex_tui__status_indicator_widget__tests__renders_with_queued_messages@macos.snap
index 5974455c89..377dd06449 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__status_indicator_widget__tests__renders_with_queued_messages@macos.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__status_indicator_widget__tests__renders_with_queued_messages@macos.snap
@@ -3,11 +3,11 @@ source: tui/src/status_indicator_widget.rs
 assertion_line: 289
 expression: terminal.backend()
 ---
-"• Working (0s • esc to interrupt)                                               "
+"■ Working (0s ■ esc to interrupt)                                               "
 "                                                                                "
-" ↳ first                                                                        "
-" ↳ second                                                                       "
-"   ⌥ + ↑ edit                                                                   "
+" > first                                                                        "
+" > second                                                                       "
+"   - + ↑ edit                                                                   "
 "                                                                                "
 "                                                                                "
 "                                                                                "
diff --git a/codex-rs/tui/src/snapshots/codex_tui__status_indicator_widget__tests__renders_with_working_header.snap b/codex-rs/tui/src/snapshots/codex_tui__status_indicator_widget__tests__renders_with_working_header.snap
index 2b80830f81..d4582cbefb 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__status_indicator_widget__tests__renders_with_working_header.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__status_indicator_widget__tests__renders_with_working_header.snap
@@ -2,5 +2,5 @@
 source: tui/src/status_indicator_widget.rs
 expression: terminal.backend()
 ---
-"• Working (0s • esc to interrupt)                                               "
+"■ Working (0s ■ esc to interrupt)                                               "
 "                                                                                "
diff --git a/codex-rs/tui/src/snapshots/codex_tui__update_prompt__tests__update_prompt_modal.snap b/codex-rs/tui/src/snapshots/codex_tui__update_prompt__tests__update_prompt_modal.snap
index 24d8831c95..e574ea660b 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__update_prompt__tests__update_prompt_modal.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__update_prompt__tests__update_prompt_modal.snap
@@ -2,7 +2,7 @@
 source: tui/src/update_prompt.rs
 expression: terminal.backend()
 ---
-  ✨ Update available! 0.0.0 -> 9.9.9
+  * Update available! 0.0.0 -> 9.9.9
 
   Release notes: https://github.com/openai/codex/releases/latest
 
diff --git a/codex-rs/tui/src/status_indicator_widget.rs b/codex-rs/tui/src/status_indicator_widget.rs
index 622c4f989e..1ab5c240ae 100644
--- a/codex-rs/tui/src/status_indicator_widget.rs
+++ b/codex-rs/tui/src/status_indicator_widget.rs
@@ -269,7 +269,7 @@ impl Renderable for StatusIndicatorWidget {
             && let Some(interrupt_binding) = self.interrupt_binding
         {
             spans.extend(vec![
-                format!("({pretty_elapsed} • ").dim(),
+                format!("({pretty_elapsed} ■ ").dim(),
                 interrupt_binding.into(),
                 " to interrupt)".dim(),
             ]);
@@ -412,7 +412,7 @@ mod tests {
             .map(ratatui::buffer::Cell::symbol)
             .collect::<String>();
 
-        assert!(line.starts_with("Working (0s • esc to interrupt)"));
+        assert!(line.starts_with("Working (0s ■ esc to interrupt)"));
     }
 
     #[test]
diff --git a/codex-rs/tui/src/streaming/controller.rs b/codex-rs/tui/src/streaming/controller.rs
index 95a3b72269..7cdb74dde1 100644
--- a/codex-rs/tui/src/streaming/controller.rs
+++ b/codex-rs/tui/src/streaming/controller.rs
@@ -703,7 +703,7 @@ impl PlanStreamController {
         let mut out_lines: Vec<HyperlinkLine> = Vec::with_capacity(/*capacity*/ 4);
         if !self.header_emitted {
             out_lines.push(HyperlinkLine::new(
-                vec!["• ".dim(), "Proposed Plan".bold()].into(),
+                vec!["■ ".dim(), "Proposed Plan".bold()].into(),
             ));
             out_lines.push(HyperlinkLine::new(Line::from(" ")));
         }
@@ -1015,7 +1015,7 @@ mod tests {
                 .transcript_lines(u16::MAX),
         );
 
-        assert_eq!(rendered, vec!["• tail without newline".to_string()]);
+        assert_eq!(rendered, vec!["■ tail without newline".to_string()]);
     }
 
     #[test]
@@ -1563,7 +1563,7 @@ mod tests {
 
     #[test]
     fn controller_live_view_matches_render_during_interleaved_table_streaming() {
-        let source = "Project updates are easier to scan when narrative and structured data alternate.\n\n| Focus Area | Owner | Priority | Status |\n|---|---|---|---|\n| Authentication cleanup | Maya | High | 80% |\n| CLI error messages | Jordan | Medium | 55% |\n| Docs refresh | Lee | Low | 30% |\n\nThe first checkpoint shows progress, but we still have open risks.\n\n| Task | Command / Artifact | Due | State |\n|---|---|---|---|\n| Run unit tests | `cargo test -p codex-core` | Today | ✅ |\n| Snapshot review | `cargo insta pending-snapshots -p codex-tui` | Today | ⏳ |\n| Changelog draft | Release template (https://replacechangelog.com/) | Tomorrow | 📝 |\n\nFinal sign-off criteria are summarized below.\n";
+        let source = "Project updates are easier to scan when narrative and structured data alternate.\n\n| Focus Area | Owner | Priority | Status |\n|---|---|---|---|\n| Authentication cleanup | Maya | High | 80% |\n| CLI error messages | Jordan | Medium | 55% |\n| Docs refresh | Lee | Low | 30% |\n\nThe first checkpoint shows progress, but we still have open risks.\n\n| Task | Command / Artifact | Due | State |\n|---|---|---|---|\n| Run unit tests | `cargo test -p codex-core` | Today | + |\n| Snapshot review | `cargo insta pending-snapshots -p codex-tui` | Today | * |\n| Changelog draft | Release template (https://replacechangelog.com/) | Tomorrow | * |\n\nFinal sign-off criteria are summarized below.\n";
         let width = Some(72usize);
         let mut ctrl = stream_controller(width);
         let mut emitted_lines: Vec<Line<'static>> = Vec::new();
diff --git a/codex-rs/tui/src/text_formatting.rs b/codex-rs/tui/src/text_formatting.rs
index a89f392ebb..845f99dae7 100644
--- a/codex-rs/tui/src/text_formatting.rs
+++ b/codex-rs/tui/src/text_formatting.rs
@@ -417,12 +417,12 @@ mod tests {
 
     #[test]
     fn test_truncate_emoji() {
-        let text = "👋🌍🚀✨💫";
+        let text = "*****";
         let truncated = truncate_text(text, /*max_graphemes*/ 3);
         assert_eq!(truncated, "...");
 
         let truncated_longer = truncate_text(text, /*max_graphemes*/ 4);
-        assert_eq!(truncated_longer, "👋...");
+        assert_eq!(truncated_longer, "*...");
     }
 
     #[test]
diff --git a/codex-rs/tui/src/update_prompt.rs b/codex-rs/tui/src/update_prompt.rs
index 8fec45590f..6041596cd4 100644
--- a/codex-rs/tui/src/update_prompt.rs
+++ b/codex-rs/tui/src/update_prompt.rs
@@ -192,7 +192,7 @@ impl WidgetRef for &UpdatePromptScreen {
 
         column.push("");
         column.push(Line::from(vec![
-            padded_emoji("  ✨").bold().cyan(),
+            padded_emoji("  *").bold().cyan(),
             "Update available!".bold(),
             " ".into(),
             format!(
