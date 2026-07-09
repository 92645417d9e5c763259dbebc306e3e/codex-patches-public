diff --git a/codex-rs/tui/src/history_cell/session.rs b/codex-rs/tui/src/history_cell/session.rs
index c63f6f746c..cbd8ddffe6 100644
--- a/codex-rs/tui/src/history_cell/session.rs
+++ b/codex-rs/tui/src/history_cell/session.rs
@@ -48,7 +48,7 @@ fn with_border_internal(
 
     let mut out = Vec::with_capacity(lines.len() + 2);
     let border_inner_width = content_width + 2;
-    out.push(vec![format!("╭{}╮", "─".repeat(border_inner_width)).dim()].into());
+    out.push(vec![format!("┌{}┐", "─".repeat(border_inner_width)).dim()].into());
 
     for line in lines.into_iter() {
         let used_width: usize = line
@@ -66,7 +66,7 @@ fn with_border_internal(
         out.push(Line::from(spans));
     }
 
-    out.push(vec![format!("╰{}╯", "─".repeat(border_inner_width)).dim()].into());
+    out.push(vec![format!("└{}┘", "─".repeat(border_inner_width)).dim()].into());
 
     out
 }
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__session_header_indicates_yolo_mode.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__session_header_indicates_yolo_mode.snap
index 04f64584f6..d2ba33df1a 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__session_header_indicates_yolo_mode.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__session_header_indicates_yolo_mode.snap
@@ -2,10 +2,10 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-╭───────────────────────────────────────╮
+┌───────────────────────────────────────┐
 │ >_ OpenAI Codex (vtest)               │
 │                                       │
 │ model:       gpt-5   /model to change │
 │ directory:   /tmp/project             │
 │ permissions: YOLO mode                │
-╰───────────────────────────────────────╯
+└───────────────────────────────────────┘
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__session_info_availability_nux_tooltip_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__session_info_availability_nux_tooltip_snapshot.snap
index ad0fc4be1c..3ff89d47e0 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__session_info_availability_nux_tooltip_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__session_info_availability_nux_tooltip_snapshot.snap
@@ -2,11 +2,11 @@
 source: tui/src/history_cell.rs
 expression: rendered
 ---
-╭─────────────────────────────────────╮
+┌─────────────────────────────────────┐
 │ >_ OpenAI Codex (v0.0.0)            │
 │                                     │
 │ model:     gpt-5   /model to change │
 │ directory: /tmp/project             │
-╰─────────────────────────────────────╯
+└─────────────────────────────────────┘
 
   Tip: Model just became available
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__standalone_unix_update_available_history_cell_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__standalone_unix_update_available_history_cell_snapshot.snap
index c8f352dbb4..4a93e5f1e1 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__standalone_unix_update_available_history_cell_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__standalone_unix_update_available_history_cell_snapshot.snap
@@ -2,10 +2,10 @@
 source: tui/src/history_cell/tests.rs
 expression: rendered
 ---
-╭─────────────────────────────────────────────────────────────────────────────────────────────────────╮
+┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
 │ ✨ Update available! 0.0.0 -> 9.9.9                                                                 │
 │ Run sh -c 'curl -fsSL https://chatgpt.com/codex/install.sh | CODEX_NON_INTERACTIVE=1 sh' to update. │
 │                                                                                                     │
 │ See full release notes:                                                                             │
 │ https://github.com/openai/codex/releases/latest                                                     │
-╰─────────────────────────────────────────────────────────────────────────────────────────────────────╯
+└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__standalone_windows_update_available_history_cell_snapshot.snap b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__standalone_windows_update_available_history_cell_snapshot.snap
index fb15a05775..a8eed3e97e 100644
--- a/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__standalone_windows_update_available_history_cell_snapshot.snap
+++ b/codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__standalone_windows_update_available_history_cell_snapshot.snap
@@ -2,11 +2,11 @@
 source: tui/src/history_cell/tests.rs
 expression: rendered
 ---
-╭────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
+┌────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
 │ ✨ Update available! 0.0.0 -> 9.9.9                                                                        │
 │ Run powershell -ExecutionPolicy Bypass -c '$env:CODEX_NON_INTERACTIVE=1; irm                               │
 │ https://chatgpt.com/codex/install.ps1 | iex' to update.                                                    │
 │                                                                                                            │
 │ See full release notes:                                                                                    │
 │ https://github.com/openai/codex/releases/latest                                                            │
-╰────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
+└────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/insert_history.rs b/codex-rs/tui/src/insert_history.rs
index 760b516421..e79d5f0b99 100644
--- a/codex-rs/tui/src/insert_history.rs
+++ b/codex-rs/tui/src/insert_history.rs
@@ -224,9 +224,9 @@ where
             // │┆                            ┆│
             // │┆                            ┆│
             // │█╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┘│
-            // │╭─Viewport───────────────────╮│
+            // │┌─Viewport───────────────────┐│
             // ││                            ││
-            // │╰────────────────────────────╯│
+            // │└────────────────────────────┘│
             // └──────────────────────────────┘
             queue!(writer, SetScrollRegion(1..area.top()))?;
 
diff --git a/codex-rs/tui/src/onboarding/auth.rs b/codex-rs/tui/src/onboarding/auth.rs
index f9392eb2e8..699a2b23c5 100644
--- a/codex-rs/tui/src/onboarding/auth.rs
+++ b/codex-rs/tui/src/onboarding/auth.rs
@@ -655,7 +655,7 @@ impl AuthModeWidget {
                 Block::default()
                     .title("API key")
                     .borders(Borders::ALL)
-                    .border_type(BorderType::Rounded)
+                    .border_type(BorderType::Plain)
                     .border_style(Style::default().fg(Color::Cyan)),
             )
             .render(input_area, buf);
diff --git a/codex-rs/tui/src/snapshots/codex_tui__app__tests__clear_ui_after_long_transcript_fresh_header_only.snap b/codex-rs/tui/src/snapshots/codex_tui__app__tests__clear_ui_after_long_transcript_fresh_header_only.snap
index 98d6015064..1363059f6f 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__app__tests__clear_ui_after_long_transcript_fresh_header_only.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__app__tests__clear_ui_after_long_transcript_fresh_header_only.snap
@@ -2,9 +2,9 @@
 source: tui/src/app.rs
 expression: rendered
 ---
-╭─────────────────────────────────────────────╮
+┌─────────────────────────────────────────────┐
 │ >_ OpenAI Codex (v<VERSION>)                │
 │                                             │
 │ model:     gpt-test high   /model to change │
 │ directory: /tmp/project                     │
-╰─────────────────────────────────────────────╯
+└─────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/snapshots/codex_tui__app__tests__clear_ui_header_fast_status_fast_capable_models.snap b/codex-rs/tui/src/snapshots/codex_tui__app__tests__clear_ui_header_fast_status_fast_capable_models.snap
index 08afd027ac..0f3edbe381 100644
--- a/codex-rs/tui/src/snapshots/codex_tui__app__tests__clear_ui_header_fast_status_fast_capable_models.snap
+++ b/codex-rs/tui/src/snapshots/codex_tui__app__tests__clear_ui_header_fast_status_fast_capable_models.snap
@@ -2,9 +2,9 @@
 source: tui/src/app.rs
 expression: rendered
 ---
-╭────────────────────────────────────────────────────╮
+┌────────────────────────────────────────────────────┐
 │ >_ OpenAI Codex (v<VERSION>)                       │
 │                                                    │
 │ model:     gpt-5.4 xhigh   fast   /model to change │
 │ directory: /tmp/project                            │
-╰────────────────────────────────────────────────────╯
+└────────────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_cached_limits_hide_credits_without_flag.snap b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_cached_limits_hide_credits_without_flag.snap
index c7d89b17aa..0f47d73b64 100644
--- a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_cached_limits_hide_credits_without_flag.snap
+++ b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_cached_limits_hide_credits_without_flag.snap
@@ -4,7 +4,7 @@ expression: sanitized
 ---
 /status
 
-╭─────────────────────────────────────────────────────────────────────────────╮
+┌─────────────────────────────────────────────────────────────────────────────┐
 │  >_ OpenAI Codex (v0.0.0)                                                   │
 │                                                                             │
 │ Visit https://chatgpt.com/codex/settings/usage for up-to-date               │
@@ -20,4 +20,4 @@ expression: sanitized
 │  5h limit:         [████████░░░░░░░░░░░░] 40% left (resets 11:32)           │
 │  Weekly limit:     [█████████████░░░░░░░] 65% left (resets 11:52)           │
 │  Warning:          limits may be stale - start new turn to refresh.         │
-╰─────────────────────────────────────────────────────────────────────────────╯
+└─────────────────────────────────────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_includes_credits_and_limits.snap b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_includes_credits_and_limits.snap
index 48fa575d1f..05074beb34 100644
--- a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_includes_credits_and_limits.snap
+++ b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_includes_credits_and_limits.snap
@@ -4,7 +4,7 @@ expression: sanitized
 ---
 /status
 
-╭─────────────────────────────────────────────────────────────────────────────╮
+┌─────────────────────────────────────────────────────────────────────────────┐
 │  >_ OpenAI Codex (v0.0.0)                                                   │
 │                                                                             │
 │ Visit https://chatgpt.com/codex/settings/usage for up-to-date               │
@@ -20,4 +20,4 @@ expression: sanitized
 │  5h limit:         [███████████░░░░░░░░░] 55% left (resets 09:25)           │
 │  Weekly limit:     [██████████████░░░░░░] 70% left (resets 09:55)           │
 │  Credits:          38 credits                                               │
-╰─────────────────────────────────────────────────────────────────────────────╯
+└─────────────────────────────────────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_includes_enterprise_monthly_credit_limit.snap b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_includes_enterprise_monthly_credit_limit.snap
index 765ad8d3a7..300ea408ba 100644
--- a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_includes_enterprise_monthly_credit_limit.snap
+++ b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_includes_enterprise_monthly_credit_limit.snap
@@ -4,7 +4,7 @@ expression: sanitized
 ---
 /status
 
-╭───────────────────────────────────────────────────────────────────────────────────╮
+┌───────────────────────────────────────────────────────────────────────────────────┐
 │  >_ OpenAI Codex (v0.0.0)                                                         │
 │                                                                                   │
 │ Visit https://chatgpt.com/codex/settings/usage for up-to-date                     │
@@ -19,4 +19,4 @@ expression: sanitized
 │  Context window:         100% left (1.2K used / 272K)                             │
 │  Monthly credit limit:   [██████████████░░░░░░] 68% left (resets 07:08 on 7 May)  │
 │                          8,000 of 25,000 credits used                             │
-╰───────────────────────────────────────────────────────────────────────────────────╯
+└───────────────────────────────────────────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_includes_forked_from.snap b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_includes_forked_from.snap
index 152575179e..0212b3acf0 100644
--- a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_includes_forked_from.snap
+++ b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_includes_forked_from.snap
@@ -4,7 +4,7 @@ expression: sanitized
 ---
 /status
 
-╭─────────────────────────────────────────────────────────────────────────────╮
+┌─────────────────────────────────────────────────────────────────────────────┐
 │  >_ OpenAI Codex (v0.0.0)                                                   │
 │                                                                             │
 │ Visit https://chatgpt.com/codex/settings/usage for up-to-date               │
@@ -20,4 +20,4 @@ expression: sanitized
 │  Token usage:      1.2K total  (800 input + 400 output)                     │
 │  Context window:   100% left (1.2K used / 272K)                             │
 │  Limits:           data not available yet                                   │
-╰─────────────────────────────────────────────────────────────────────────────╯
+└─────────────────────────────────────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_includes_monthly_limit.snap b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_includes_monthly_limit.snap
index 7a4f58a823..271b4e7042 100644
--- a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_includes_monthly_limit.snap
+++ b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_includes_monthly_limit.snap
@@ -4,7 +4,7 @@ expression: sanitized
 ---
 /status
 
-╭─────────────────────────────────────────────────────────────────────────────╮
+┌─────────────────────────────────────────────────────────────────────────────┐
 │  >_ OpenAI Codex (v0.0.0)                                                   │
 │                                                                             │
 │ Visit https://chatgpt.com/codex/settings/usage for up-to-date               │
@@ -18,4 +18,4 @@ expression: sanitized
 │  Token usage:      1.2K total  (800 input + 400 output)                     │
 │  Context window:   100% left (1.2K used / 272K)                             │
 │  Monthly limit:    [██████████████████░░] 88% left (resets 07:08 on 7 May)  │
-╰─────────────────────────────────────────────────────────────────────────────╯
+└─────────────────────────────────────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_includes_reasoning_details.snap b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_includes_reasoning_details.snap
index 96b2ed1648..1d176fef81 100644
--- a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_includes_reasoning_details.snap
+++ b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_includes_reasoning_details.snap
@@ -4,7 +4,7 @@ expression: sanitized
 ---
 /status
 
-╭───────────────────────────────────────────────────────────────────────────╮
+┌───────────────────────────────────────────────────────────────────────────┐
 │  >_ OpenAI Codex (v0.0.0)                                                 │
 │                                                                           │
 │ Visit https://chatgpt.com/codex/settings/usage for up-to-date             │
@@ -19,4 +19,4 @@ expression: sanitized
 │  Context window:   100% left (2.25K used / 272K)                          │
 │  5h limit:         [██████░░░░░░░░░░░░░░] 28% left (resets 03:14)         │
 │  Weekly limit:     [███████████░░░░░░░░░] 55% left (resets 03:24)         │
-╰───────────────────────────────────────────────────────────────────────────╯
+└───────────────────────────────────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_active_user_defined_profile.snap b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_active_user_defined_profile.snap
index 4604b26f7e..fc00a1fa2f 100644
--- a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_active_user_defined_profile.snap
+++ b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_active_user_defined_profile.snap
@@ -4,7 +4,7 @@ expression: sanitized
 ---
 /status
 
-╭───────────────────────────────────────────────────────────────────────╮
+┌───────────────────────────────────────────────────────────────────────┐
 │  >_ OpenAI Codex (v0.0.0)                                             │
 │                                                                       │
 │ Visit https://chatgpt.com/codex/settings/usage for up-to-date         │
@@ -18,4 +18,4 @@ expression: sanitized
 │  Token usage:      0 total  (0 input + 0 output)                      │
 │  Context window:   100% left (0 used / 272K)                          │
 │  Limits:           data not available yet                             │
-╰───────────────────────────────────────────────────────────────────────╯
+└───────────────────────────────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_auto_review_permissions.snap b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_auto_review_permissions.snap
index c739d55075..922b03c1a0 100644
--- a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_auto_review_permissions.snap
+++ b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_auto_review_permissions.snap
@@ -4,7 +4,7 @@ expression: sanitized
 ---
 /status
 
-╭───────────────────────────────────────────────────────────────────────╮
+┌───────────────────────────────────────────────────────────────────────┐
 │  >_ OpenAI Codex (v0.0.0)                                             │
 │                                                                       │
 │ Visit https://chatgpt.com/codex/settings/usage for up-to-date         │
@@ -18,4 +18,4 @@ expression: sanitized
 │  Token usage:      0 total  (0 input + 0 output)                      │
 │  Context window:   100% left (0 used / 272K)                          │
 │  Limits:           data not available yet                             │
-╰───────────────────────────────────────────────────────────────────────╯
+└───────────────────────────────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_chatgpt_plan_without_email.snap b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_chatgpt_plan_without_email.snap
index 4ac5239b94..48bfc89e18 100644
--- a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_chatgpt_plan_without_email.snap
+++ b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_chatgpt_plan_without_email.snap
@@ -4,7 +4,7 @@ expression: sanitized
 ---
 /status
 
-╭──────────────────────────────────────────────────────────────────────────╮
+┌──────────────────────────────────────────────────────────────────────────┐
 │  >_ OpenAI Codex (v0.0.0)                                                │
 │                                                                          │
 │ Visit https://chatgpt.com/codex/settings/usage for up-to-date            │
@@ -17,4 +17,4 @@ expression: sanitized
 │  Account:       Enterprise                                               │
 │                                                                          │
 │  Limits:        data not available yet                                   │
-╰──────────────────────────────────────────────────────────────────────────╯
+└──────────────────────────────────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_missing_limits_message.snap b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_missing_limits_message.snap
index 533be27976..1f919e4d49 100644
--- a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_missing_limits_message.snap
+++ b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_missing_limits_message.snap
@@ -4,7 +4,7 @@ expression: sanitized
 ---
 /status
 
-╭─────────────────────────────────────────────────────────────────────────────╮
+┌─────────────────────────────────────────────────────────────────────────────┐
 │  >_ OpenAI Codex (v0.0.0)                                                   │
 │                                                                             │
 │ Visit https://chatgpt.com/codex/settings/usage for up-to-date               │
@@ -18,4 +18,4 @@ expression: sanitized
 │  Token usage:      750 total  (500 input + 250 output)                      │
 │  Context window:   100% left (750 used / 272K)                              │
 │  Limits:           data not available yet                                   │
-╰─────────────────────────────────────────────────────────────────────────────╯
+└─────────────────────────────────────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_refreshing_limits_notice.snap b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_refreshing_limits_notice.snap
index 631982bcf9..22f76cb2d4 100644
--- a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_refreshing_limits_notice.snap
+++ b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_refreshing_limits_notice.snap
@@ -4,7 +4,7 @@ expression: sanitized
 ---
 /status
 
-╭─────────────────────────────────────────────────────────────────────────────╮
+┌─────────────────────────────────────────────────────────────────────────────┐
 │  >_ OpenAI Codex (v0.0.0)                                                   │
 │                                                                             │
 │ Visit https://chatgpt.com/codex/settings/usage for up-to-date               │
@@ -19,4 +19,4 @@ expression: sanitized
 │  Context window:   100% left (750 used / 272K)                              │
 │  5h limit:         [███████████░░░░░░░░░] 55% left (resets 08:24)           │
 │  Weekly limit:     [██████████████░░░░░░] 70% left (resets 08:54)           │
-╰─────────────────────────────────────────────────────────────────────────────╯
+└─────────────────────────────────────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_stale_limits_message.snap b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_stale_limits_message.snap
index 8facd56275..9ee62e9c20 100644
--- a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_stale_limits_message.snap
+++ b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_stale_limits_message.snap
@@ -4,7 +4,7 @@ expression: sanitized
 ---
 /status
 
-╭─────────────────────────────────────────────────────────────────────────────╮
+┌─────────────────────────────────────────────────────────────────────────────┐
 │  >_ OpenAI Codex (v0.0.0)                                                   │
 │                                                                             │
 │ Visit https://chatgpt.com/codex/settings/usage for up-to-date               │
@@ -20,4 +20,4 @@ expression: sanitized
 │  5h limit:         [██████░░░░░░░░░░░░░░] 28% left (resets 03:14)           │
 │  Weekly limit:     [████████████░░░░░░░░] 60% left (resets 03:34)           │
 │  Warning:          limits may be stale - start new turn to refresh.         │
-╰─────────────────────────────────────────────────────────────────────────────╯
+└─────────────────────────────────────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_unavailable_limits_message.snap b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_unavailable_limits_message.snap
index d46a483e4b..cd3f45df1d 100644
--- a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_unavailable_limits_message.snap
+++ b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_shows_unavailable_limits_message.snap
@@ -4,7 +4,7 @@ expression: sanitized
 ---
 /status
 
-╭─────────────────────────────────────────────────────────────────────────────╮
+┌─────────────────────────────────────────────────────────────────────────────┐
 │  >_ OpenAI Codex (v0.0.0)                                                   │
 │                                                                             │
 │ Visit https://chatgpt.com/codex/settings/usage for up-to-date               │
@@ -18,4 +18,4 @@ expression: sanitized
 │  Token usage:      750 total  (500 input + 250 output)                      │
 │  Context window:   100% left (750 used / 272K)                              │
 │  Limits:           not available for this account                           │
-╰─────────────────────────────────────────────────────────────────────────────╯
+└─────────────────────────────────────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_treats_refreshing_empty_limits_as_unavailable.snap b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_treats_refreshing_empty_limits_as_unavailable.snap
index d46a483e4b..cd3f45df1d 100644
--- a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_treats_refreshing_empty_limits_as_unavailable.snap
+++ b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_treats_refreshing_empty_limits_as_unavailable.snap
@@ -4,7 +4,7 @@ expression: sanitized
 ---
 /status
 
-╭─────────────────────────────────────────────────────────────────────────────╮
+┌─────────────────────────────────────────────────────────────────────────────┐
 │  >_ OpenAI Codex (v0.0.0)                                                   │
 │                                                                             │
 │ Visit https://chatgpt.com/codex/settings/usage for up-to-date               │
@@ -18,4 +18,4 @@ expression: sanitized
 │  Token usage:      750 total  (500 input + 250 output)                      │
 │  Context window:   100% left (750 used / 272K)                              │
 │  Limits:           not available for this account                           │
-╰─────────────────────────────────────────────────────────────────────────────╯
+└─────────────────────────────────────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_truncates_in_narrow_terminal.snap b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_truncates_in_narrow_terminal.snap
index 6b28b53b62..3935a6bdef 100644
--- a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_truncates_in_narrow_terminal.snap
+++ b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_truncates_in_narrow_terminal.snap
@@ -4,7 +4,7 @@ expression: sanitized
 ---
 /status
 
-╭────────────────────────────────────────────────────────────────────╮
+┌────────────────────────────────────────────────────────────────────┐
 │  >_ OpenAI Codex (v0.0.0)                                          │
 │                                                                    │
 │ Visit https://chatgpt.com/codex/settings/usage for up-to-date      │
@@ -18,4 +18,4 @@ expression: sanitized
 │  Token usage:      1.9K total  (1K input + 900 output)             │
 │  Context window:   100% left (2.25K used / 272K)                   │
 │  5h limit:         [██████░░░░░░░░░░░░░░] 28% left (resets 03:14)  │
-╰────────────────────────────────────────────────────────────────────╯
+└────────────────────────────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_uses_default_reasoning_when_config_empty.snap b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_uses_default_reasoning_when_config_empty.snap
index 9683beed97..498516af04 100644
--- a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_uses_default_reasoning_when_config_empty.snap
+++ b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_uses_default_reasoning_when_config_empty.snap
@@ -4,7 +4,7 @@ expression: sanitized
 ---
 /status
 
-╭─────────────────────────────────────────────────────────────────────────────╮
+┌─────────────────────────────────────────────────────────────────────────────┐
 │  >_ OpenAI Codex (v0.0.0)                                                   │
 │                                                                             │
 │ Visit https://chatgpt.com/codex/settings/usage for up-to-date               │
@@ -21,4 +21,4 @@ expression: sanitized
 │  Token usage:      750 total  (500 input + 250 output)                      │
 │  Context window:   100% left (750 used / 272K)                              │
 │  Limits:           data not available yet                                   │
-╰─────────────────────────────────────────────────────────────────────────────╯
+└─────────────────────────────────────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_uses_generic_limit_labels_for_unsupported_windows.snap b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_uses_generic_limit_labels_for_unsupported_windows.snap
index 6b6fad683b..d7ec83ea6e 100644
--- a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_uses_generic_limit_labels_for_unsupported_windows.snap
+++ b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_uses_generic_limit_labels_for_unsupported_windows.snap
@@ -4,7 +4,7 @@ expression: sanitized
 ---
 /status
 
-╭──────────────────────────────────────────────────────────────────────────────╮
+┌──────────────────────────────────────────────────────────────────────────────┐
 │  >_ OpenAI Codex (v0.0.0)                                                    │
 │                                                                              │
 │ Visit https://chatgpt.com/codex/settings/usage for up-to-date                │
@@ -21,4 +21,4 @@ expression: sanitized
 │                           (resets 07:08 on 7 May)                            │
 │  Secondary usage limit:   [██████████░░░░░░░░░░] 50% left                    │
 │                           (resets 07:08 on 8 May)                            │
-╰──────────────────────────────────────────────────────────────────────────────╯
+└──────────────────────────────────────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_wraps_enterprise_monthly_credit_details_in_narrow_terminal.snap b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_wraps_enterprise_monthly_credit_details_in_narrow_terminal.snap
index cf6fa2c2ec..cbc671fc17 100644
--- a/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_wraps_enterprise_monthly_credit_details_in_narrow_terminal.snap
+++ b/codex-rs/tui/src/status/snapshots/codex_tui__status__tests__status_snapshot_wraps_enterprise_monthly_credit_details_in_narrow_terminal.snap
@@ -4,7 +4,7 @@ expression: sanitized
 ---
 /status
 
-╭────────────────────────────────────────────╮
+┌────────────────────────────────────────────┐
 │  >_ OpenAI Codex (v0.0.0)                  │
 │                                            │
 │ Visit                                      │
@@ -24,4 +24,4 @@ expression: sanitized
 │                          7 May)            │
 │                          8,000 of 25,000   │
 │                          credits used      │
-╰────────────────────────────────────────────╯
+└────────────────────────────────────────────┘
diff --git a/codex-rs/tui/src/status/tests.rs b/codex-rs/tui/src/status/tests.rs
index 50ef2c5000..c0365a5247 100644
--- a/codex-rs/tui/src/status/tests.rs
+++ b/codex-rs/tui/src/status/tests.rs
@@ -177,7 +177,7 @@ fn render_lines(lines: &[Line<'static>]) -> Vec<String> {
 fn sanitize_directory(lines: Vec<String>) -> Vec<String> {
     let frame_width = lines
         .iter()
-        .find(|line| line.starts_with('╭'))
+        .find(|line| line.starts_with('┌'))
         .map(|line| UnicodeWidthStr::width(line.as_str()));
     lines
         .into_iter()
