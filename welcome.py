import streamlit as st


# =========================================================================
# SCOPED LIGHT-THEME OVERRIDE — "editor file" redesign
# -------------------------------------------------------------------------
# app.py injects a global dark theme for the workspace tab. This page still
# needs its own look — but instead of a marketing-style nav+card grid, the
# whole page is framed as a single open source file in an editor: a tab
# bar, line numbers, a docstring hero, a dict-literal stat block, and the
# 4-step guide rendered as an actual function body. Everything is scoped
# under #ph-welcome-root so the dark workspace tab is untouched.
# =========================================================================
def _inject_welcome_theme():
    st.markdown(
        """
        <style>
        #ph-welcome-root {
            --w-bg: #f5f7fa;
            --w-editor: #1c2333;
            --w-editor-line: #283150;
            --w-editor-text: #c9d4ec;
            --w-card: #ffffff;
            --w-border: #e3e8f0;
            --w-text: #1a2233;
            --w-text-muted: #5b6478;
            --w-text-faint: #97a1b5;
            --w-green: #10b87e;
            --w-blue: #2f7fe0;
            --w-orange: #e0a82f;
            --w-radius: 14px;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        #ph-welcome-root * { box-sizing: border-box; }

        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&display=swap');

        #ph-welcome-root {
            background: var(--w-bg);
            border-radius: var(--w-radius);
            padding: 0;
            margin: -1rem -1rem 0 -1rem;
        }
        #ph-welcome-root, #ph-welcome-root p,
        #ph-welcome-root div, #ph-welcome-root li {
            color: var(--w-text);
        }
        /* span color is reset narrowly (not globally) so our syntax-highlight
           color classes below (.wh-str, .wh-num, .wh-comment, etc.) are never
           shadowed by a same-or-lower-specificity catch-all */
        #ph-welcome-root span:not([class^="wh-"]) {
            color: var(--w-text);
        }
        #ph-welcome-root h1, #ph-welcome-root h2, #ph-welcome-root h3 {
            color: var(--w-text) !important;
        }
        .wh-mono { font-family: 'JetBrains Mono', 'SF Mono', 'Cascadia Code', Consolas, monospace; }

        @keyframes whFadeIn {
            from { opacity: 0; transform: translateY(6px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        .wh-fade { animation: whFadeIn 0.45s cubic-bezier(0.16,1,0.3,1) both; }
        .wh-d1 { animation-delay: 0.04s; }
        .wh-d2 { animation-delay: 0.10s; }
        .wh-d3 { animation-delay: 0.16s; }
        .wh-d4 { animation-delay: 0.22s; }
        .wh-d5 { animation-delay: 0.28s; }

        /* ---------- THE FILE FRAME (signature element) ---------- */
        .wh-file {
            background: var(--w-card);
            border: 1px solid var(--w-border);
            border-radius: var(--w-radius);
            overflow: hidden;
            box-shadow: 0 1px 2px rgba(16,24,40,0.05);
            margin-bottom: 1.4rem;
        }

        /* tab bar */
        .wh-tabbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: var(--w-editor);
            padding: 0.65rem 1rem;
        }
        .wh-tabbar-left { display: flex; align-items: center; gap: 0.9rem; }
        .wh-dots { display: flex; gap: 0.4rem; }
        .wh-dot { width: 10px; height: 10px; border-radius: 50%; }
        .wh-dot-r { background: #ff5f57; }
        .wh-dot-y { background: #febc2e; }
        .wh-dot-g { background: #28c840; }
        .wh-filename {
            font-size: 0.82rem;
            font-weight: 500;
            color: var(--w-editor-text);
            letter-spacing: 0.01em;
        }
        .wh-filename .wh-modified {
            display: inline-block;
            width: 7px; height: 7px;
            border-radius: 50%;
            background: var(--w-orange);
            margin-left: 0.5rem;
        }
        .wh-branch {
            display: flex;
            align-items: center;
            gap: 0.35rem;
            font-size: 0.74rem;
            font-weight: 600;
            color: #9fb4e8;
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 999px;
            padding: 0.25rem 0.7rem 0.25rem 0.55rem;
        }

        /* code body */
        .wh-code {
            background: var(--w-editor);
            padding: 1.6rem 0 1.8rem 0;
            overflow-x: auto;
        }
        .wh-line {
            display: flex;
            padding: 0 1.4rem;
        }
        .wh-lineno {
            flex: 0 0 2.4rem;
            color: #5e6996;
            font-size: 0.82rem;
            user-select: none;
            text-align: right;
            padding-right: 1.1rem;
        }
        .wh-linecontent {
            flex: 1 1 auto;
            min-width: 0;
            font-size: 0.95rem;
            line-height: 1.85;
            color: var(--w-editor-text);
            white-space: nowrap;
        }
        .wh-hero-line, .wh-hero-tagline {
            white-space: normal;
        }
        .wh-str { color: #f0b86e; }
        .wh-kw { color: #c792ea; }
        .wh-num { color: #82d4c0; }
        .wh-key { color: #7fc8f8; }
        .wh-comment { color: #6b7694; }
        .wh-fn { color: #82d4c0; }
        .wh-punct { color: #8a96b8; }

        .wh-hero-line {
            font-size: 1.5rem !important;
            font-weight: 700;
            line-height: 1.5 !important;
        }
        .wh-hero-tagline { font-size: 1.02rem !important; color: #9aa6c8 !important; }

        /* glyph row inside the file (logo-echo, restrained) */
        .wh-glyphrow {
            display: flex;
            align-items: center;
            gap: 0.7rem;
            padding: 0.5rem 1.4rem 0 1.4rem;
        }
        .wh-glyph {
            flex: 0 0 auto;
            width: 30px; height: 34px;
            display: flex; align-items: center; justify-content: center;
        }
        .wh-glyphrow-text {
            font-size: 0.86rem;
            color: var(--w-editor-text);
            opacity: 0.65;
        }

        /* ---------- SECTION LABEL = COMMENT ---------- */
        .wh-section-comment {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.84rem;
            font-weight: 500;
            color: var(--w-text-faint);
            margin: 1.7rem 0 0.7rem 0.2rem;
        }
        .wh-section-comment .wh-hash { color: var(--w-green); font-weight: 700; }

        /* ---------- MISSION BLOCK (docstring card) ---------- */
        .wh-docstring-card {
            background: var(--w-card);
            border: 1px solid var(--w-border);
            border-left: 3px solid var(--w-green);
            border-radius: var(--w-radius);
            padding: 1.4rem 1.6rem;
            margin-bottom: 0.4rem;
            box-shadow: 0 1px 2px rgba(16,24,40,0.04);
        }
        .wh-docstring-quote {
            font-family: 'JetBrains Mono', monospace;
            color: var(--w-green);
            font-size: 0.85rem;
            margin-bottom: 0.55rem;
            font-weight: 600;
        }
        .wh-docstring-text {
            font-size: 0.95rem;
            color: var(--w-text-muted);
            line-height: 1.65;
        }
        .wh-docstring-text strong { color: var(--w-text); }

        /* ---------- CONTRIBUTION FUNCTION BLOCK ---------- */
        .wh-fnblock {
            background: var(--w-editor);
            border-radius: var(--w-radius);
            padding: 1.5rem 0 1.6rem 0;
            box-shadow: 0 1px 2px rgba(16,24,40,0.04);
            margin-bottom: 0.4rem;
        }
        .wh-fn-line {
            display: flex;
            padding: 0.6rem 1.4rem;
            align-items: baseline;
            gap: 1.1rem;
            flex-wrap: wrap;
        }
        .wh-fn-call {
            font-family: 'JetBrains Mono', 'SF Mono', 'Cascadia Code', Consolas, monospace;
            font-size: 0.92rem;
            font-weight: 600;
            color: #82d4c0;
            flex: 0 0 auto;
            white-space: nowrap;
            min-width: 9.5rem;
        }
        .wh-fn-call .wh-blue { color: #7fc8f8; }
        .wh-fn-desc {
            flex: 1 1 240px;
            font-size: 0.86rem;
            color: #9aa6c8;
            line-height: 1.55;
        }
        .wh-fn-desc strong { color: #e3e8f7; }
        .wh-fn-divider {
            border-top: 1px solid rgba(255,255,255,0.06);
            margin: 0 1.4rem;
        }

        /* responsive */
        @media (max-width: 640px) {
            .wh-hero-line { font-size: 1.15rem !important; }
            .wh-lineno { flex: 0 0 1.7rem; padding-right: 0.6rem; }
            .wh-fn-line { flex-direction: column; gap: 0.3rem; }
            .wh-fn-call { min-width: 0; flex-basis: auto; }
            .wh-fn-desc { flex-basis: auto; }
        }

        /* reduced motion */
        @media (prefers-reduced-motion: reduce) {
            .wh-fade { animation: none !important; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _mini_glyph_svg():
    """Small restrained echo of the shield/snake logo mark — not a recreation,
    just a nod via the brace + gradient motif, kept tiny and quiet."""
    return """
    <div class="wh-glyph">
        <svg width="26" height="30" viewBox="0 0 26 30" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <linearGradient id="whMiniGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#10b87e"/>
                    <stop offset="100%" stop-color="#2f7fe0"/>
                </linearGradient>
            </defs>
            <path d="M13 1 L24 6 V18 C24 24 19 28 13 29 C7 28 2 24 2 18 V6 Z"
                  fill="url(#whMiniGrad)" opacity="0.95"/>
            <text x="13" y="19" text-anchor="middle" font-family="'JetBrains Mono', 'SF Mono', Consolas, monospace"
                  font-size="11" font-weight="700" fill="#ffffff">{}</text>
        </svg>
    </div>
    """


def render_welcome_page(project_map):
    """
    project_map: dict of { display_label: metadata_dict } built in app.py,
    where each metadata_dict has at least 'limitations' (list) and 'challenge'.
    Real stats are derived directly from this — nothing here is hardcoded.
    """
    total_repos = len(project_map)
    total_open_challenges = sum(len(meta.get("limitations", [])) for meta in project_map.values())
    # "Patches merged" isn't tracked by the file-driven system yet (no PR/commit
    # history is read from disk) — until Phase 3/4 of the roadmap wires in the
    # GitHub REST API, we report the number of modules that currently ship with
    # zero documented limitations as a stand-in proxy for "clean / patched" repos.
    patches_merged = sum(1 for meta in project_map.values() if not meta.get("limitations"))
    # Likewise, "community pull requests" has no local data source yet — shown
    # as a placeholder until the roadmap's GitHub API integration lands.
    community_prs_display = "None  # pending GitHub API integration"

    _inject_welcome_theme()

    st.markdown('<div id="ph-welcome-root">', unsafe_allow_html=True)

    # ================= THE FILE: tab bar + docstring hero + stats dict =================
    st.markdown(
        f"""
        <div class="wh-file wh-fade wh-d1">
            <div class="wh-tabbar">
                <div class="wh-tabbar-left">
                    <div class="wh-dots">
                        <span class="wh-dot wh-dot-r"></span>
                        <span class="wh-dot wh-dot-y"></span>
                        <span class="wh-dot wh-dot-g"></span>
                    </div>
                    <span class="wh-filename wh-mono">welcome.py<span class="wh-modified"></span></span>
                </div>
                <div class="wh-branch wh-mono">⎇ main</div>
            </div>
            <div class="wh-code">
                <div class="wh-line">
                    <span class="wh-lineno wh-mono">1</span>
                    <span class="wh-linecontent wh-mono"><span class="wh-punct">&quot;&quot;&quot;</span></span>
                </div>
                <div class="wh-line">
                    <span class="wh-lineno wh-mono">2</span>
                    <span class="wh-linecontent wh-mono wh-hero-line">PySource Hub</span>
                </div>
                <div class="wh-line">
                    <span class="wh-lineno wh-mono">3</span>
                    <span class="wh-linecontent wh-mono wh-hero-tagline">Read real, working code. Find what's broken. Patch it live.</span>
                </div>
                <div class="wh-line">
                    <span class="wh-lineno wh-mono">4</span>
                    <span class="wh-linecontent wh-mono"><span class="wh-punct">&quot;&quot;&quot;</span></span>
                </div>
                <div class="wh-line">
                    <span class="wh-lineno wh-mono">5</span>
                    <span class="wh-linecontent wh-mono">&nbsp;</span>
                </div>
                <div class="wh-line">
                    <span class="wh-lineno wh-mono">6</span>
                    <span class="wh-linecontent wh-mono"><span class="wh-key">STATS</span> <span class="wh-punct">=</span> <span class="wh-punct">{{</span></span>
                </div>
                <div class="wh-line">
                    <span class="wh-lineno wh-mono">7</span>
                    <span class="wh-linecontent wh-mono">&nbsp;&nbsp;&nbsp;&nbsp;<span class="wh-str">'active_repos'</span><span class="wh-punct">:</span> <span class="wh-num">{total_repos}</span><span class="wh-punct">,</span>&nbsp;&nbsp;<span class="wh-comment"># catalog modules loaded</span></span>
                </div>
                <div class="wh-line">
                    <span class="wh-lineno wh-mono">8</span>
                    <span class="wh-linecontent wh-mono">&nbsp;&nbsp;&nbsp;&nbsp;<span class="wh-str">'patches_merged'</span><span class="wh-punct">:</span> <span class="wh-num">{patches_merged}</span><span class="wh-punct">,</span>&nbsp;&nbsp;<span class="wh-comment"># modules with zero open issues</span></span>
                </div>
                <div class="wh-line">
                    <span class="wh-lineno wh-mono">9</span>
                    <span class="wh-linecontent wh-mono">&nbsp;&nbsp;&nbsp;&nbsp;<span class="wh-str">'open_challenges'</span><span class="wh-punct">:</span> <span class="wh-num">{total_open_challenges}</span><span class="wh-punct">,</span>&nbsp;&nbsp;<span class="wh-comment"># limitations across all modules</span></span>
                </div>
                <div class="wh-line">
                    <span class="wh-lineno wh-mono">10</span>
                    <span class="wh-linecontent wh-mono">&nbsp;&nbsp;&nbsp;&nbsp;<span class="wh-str">'community_prs'</span><span class="wh-punct">:</span> <span class="wh-kw">{community_prs_display}</span></span>
                </div>
                <div class="wh-line">
                    <span class="wh-lineno wh-mono">11</span>
                    <span class="wh-linecontent wh-mono"><span class="wh-punct">}}</span></span>
                </div>
                <div class="wh-line" style="margin-top: 0.3rem;">
                    <span class="wh-lineno wh-mono">&nbsp;</span>
                    <span class="wh-linecontent wh-mono">&nbsp;</span>
                </div>
                <div class="wh-glyphrow">{_mini_glyph_svg()}<span class="wh-glyphrow-text">An open-source Python micro-CMS &amp; practice sandbox.</span></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ================= CORE MISSION — comment + docstring card =================
    st.markdown(
        '<div class="wh-section-comment wh-fade wh-d2"><span class="wh-hash"># </span>core mission</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="wh-docstring-card wh-fade wh-d2">
            <div class="wh-docstring-quote">"Read-First, Patch-Second."</div>
            <div class="wh-docstring-text">
                Traditional platforms focus on competitive coding inside isolated browser
                sandboxes. PySource Hub is engineered to bridge the gap between classroom
                syntax and professional development — students enter an active,
                production-ready environment to study working blueprints, discover
                documented architectural limitations, and submit functional upgrades using
                real-world Git-Flow workflows.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ================= CONTRIBUTION WORKFLOW — as an actual function body =================
    st.markdown(
        '<div class="wh-section-comment wh-fade wh-d3"><span class="wh-hash"># </span>contribution workflow</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="wh-fnblock wh-fade wh-d3">
            <div class="wh-fn-line">
                <span class="wh-fn-call wh-mono">git_clone<span class="wh-blue">()</span></span>
                <span class="wh-fn-desc"><strong>Select a repository</strong> — pick a project from the sidebar index dropdown.</span>
            </div>
            <div class="wh-fn-divider"></div>
            <div class="wh-fn-line">
                <span class="wh-fn-call wh-mono">audit<span class="wh-blue">(limitations)</span></span>
                <span class="wh-fn-desc"><strong>Audit flaws</strong> — analyze the documented bugs or architectural limitations.</span>
            </div>
            <div class="wh-fn-divider"></div>
            <div class="wh-fn-line">
                <span class="wh-fn-call wh-mono">fork<span class="wh-blue">().patch(bug)</span></span>
                <span class="wh-fn-desc"><strong>Fork &amp; code</strong> — link to GitHub, fork the repository, and patch the limitation locally.</span>
            </div>
            <div class="wh-fn-divider"></div>
            <div class="wh-fn-line">
                <span class="wh-fn-call wh-mono">git_push<span class="wh-blue">() → PR</span></span>
                <span class="wh-fn-desc"><strong>Pull request</strong> — submit your code review request. Once merged, your optimized logic replaces the blueprint live.</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)  # close #ph-welcome-root