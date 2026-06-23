import streamlit as st


# =========================================================================
# SCOPED LIGHT-THEME OVERRIDE
# -------------------------------------------------------------------------
# app.py injects a global dark theme for the workspace tab. This page needs
# to look like a bright, light-mode product page instead — so everything
# below is scoped under #ph-welcome-root and wrapped in a container that
# carries that id, overriding only what's needed without touching the
# dark workspace tab's styling.
# =========================================================================
def _inject_welcome_theme():
    st.markdown(
        """
        <style>
        #ph-welcome-root {
            --w-bg: #ffffff;
            --w-canvas: #f7f9fc;
            --w-card: #eef3fb;
            --w-card-alt: #ffffff;
            --w-border: #e3e8f0;
            --w-text: #1a2233;
            --w-text-muted: #5b6478;
            --w-text-faint: #8b94a7;
            --w-accent: #4f6df5;
            --w-accent-soft: #e8edff;
            --w-pill-bg: #f1f4f9;
            --w-radius: 16px;
            --w-radius-sm: 10px;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        /* Neutralize the dark app background just for this tab's content area */
        #ph-welcome-root {
            background: var(--w-bg);
            border-radius: var(--w-radius);
            padding: 0;
            margin: -1rem -1rem 0 -1rem;
        }
        #ph-welcome-root, #ph-welcome-root p, #ph-welcome-root span,
        #ph-welcome-root div, #ph-welcome-root li {
            color: var(--w-text);
        }
        #ph-welcome-root h1, #ph-welcome-root h2, #ph-welcome-root h3 {
            color: var(--w-text) !important;
        }

        @keyframes whFadeIn {
            from { opacity: 0; transform: translateY(8px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        .wh-fade { animation: whFadeIn 0.5s cubic-bezier(0.16,1,0.3,1) both; }
        .wh-d1 { animation-delay: 0.05s; }
        .wh-d2 { animation-delay: 0.12s; }
        .wh-d3 { animation-delay: 0.19s; }
        .wh-d4 { animation-delay: 0.26s; }

        /* ---------- TOP NAV ---------- */
        .wh-nav {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 1rem 1.6rem;
            background: var(--w-card-alt);
            border: 1px solid var(--w-border);
            border-radius: var(--w-radius);
            margin-bottom: 1.6rem;
            box-shadow: 0 1px 2px rgba(16,24,40,0.04);
        }
        .wh-nav-left {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            font-weight: 700;
            font-size: 1.05rem;
            color: var(--w-text);
        }
        .wh-nav-logo {
            width: 28px; height: 28px;
            border-radius: 8px;
            background: linear-gradient(135deg, #4f6df5, #7c5cf0);
            flex-shrink: 0;
        }
        .wh-nav-links {
            display: flex;
            align-items: center;
            gap: 1.6rem;
            font-size: 0.92rem;
            font-weight: 500;
            color: var(--w-text-muted);
        }
        .wh-nav-links span { cursor: default; }
        .wh-nav-cta {
            display: flex;
            align-items: center;
            gap: 0.4rem;
            font-size: 0.86rem;
            font-weight: 600;
            color: var(--w-text);
            background: var(--w-pill-bg);
            border: 1px solid var(--w-border);
            border-radius: 999px;
            padding: 0.45rem 1rem;
            text-decoration: none !important;
            transition: all 0.2s ease;
        }
        .wh-nav-cta:hover {
            border-color: var(--w-accent);
            background: var(--w-accent-soft);
            color: var(--w-accent);
        }

        /* ---------- STAT CARD GRID ---------- */
        .wh-stat-card {
            background: var(--w-card);
            border-radius: var(--w-radius);
            padding: 1.3rem 1.5rem;
            margin-bottom: 1.1rem;
            transition: transform 0.22s ease, box-shadow 0.22s ease;
        }
        .wh-stat-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 24px -10px rgba(79,109,245,0.35);
        }
        .wh-stat-label {
            font-size: 0.82rem;
            font-weight: 600;
            color: var(--w-text-muted);
            margin-bottom: 0.5rem;
        }
        .wh-stat-value {
            font-size: 2.1rem;
            font-weight: 800;
            color: var(--w-text);
            line-height: 1;
        }
        .wh-stat-sub {
            font-size: 0.78rem;
            color: var(--w-text-faint);
            margin-top: 0.3rem;
        }

        /* ---------- HUB ICON GRAPHIC ---------- */
        .wh-hub-wrap {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            min-height: 180px;
        }

        /* ---------- WELCOME CARD ---------- */
        .wh-welcome-card {
            background: var(--w-card-alt);
            border: 1px solid var(--w-border);
            border-radius: var(--w-radius);
            padding: 1.5rem 1.6rem;
            height: 100%;
            box-shadow: 0 1px 2px rgba(16,24,40,0.04);
        }
        .wh-welcome-title {
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--w-text);
            margin-bottom: 0.6rem;
        }
        .wh-welcome-text {
            font-size: 0.88rem;
            color: var(--w-text-muted);
            line-height: 1.55;
            margin-bottom: 1.3rem;
        }

        /* ---------- ARCHITECTURE DIAGRAM ---------- */
        .wh-diagram {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.4rem;
            background: var(--w-canvas);
            border: 1px solid var(--w-border);
            border-radius: var(--w-radius-sm);
            padding: 1.1rem 0.9rem;
        }
        .wh-diagram-node {
            flex: 1;
            text-align: center;
            font-size: 0.72rem;
            font-weight: 600;
            color: var(--w-text-muted);
        }
        .wh-diagram-box {
            background: #ffffff;
            border: 1px solid var(--w-border);
            border-radius: 8px;
            padding: 0.55rem 0.4rem;
            margin-bottom: 0.4rem;
            font-size: 1.3rem;
            line-height: 1;
        }
        .wh-diagram-arrow {
            flex: 0 0 auto;
            color: var(--w-accent);
            font-size: 1.1rem;
            font-weight: 700;
            padding-bottom: 1.6rem;
        }

        /* ---------- SECTION BELOW THE FOLD ---------- */
        .wh-section-label {
            font-size: 0.78rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--w-text-faint);
            margin: 1.8rem 0 0.8rem 0;
        }
        .wh-body-card {
            background: var(--w-card-alt);
            border: 1px solid var(--w-border);
            border-radius: var(--w-radius);
            padding: 1.4rem 1.6rem;
            margin-bottom: 1rem;
            box-shadow: 0 1px 2px rgba(16,24,40,0.04);
        }
        .wh-body-text {
            font-size: 0.93rem;
            color: var(--w-text-muted);
            line-height: 1.6;
        }
        .wh-step {
            display: flex;
            gap: 0.8rem;
            align-items: flex-start;
            padding: 0.65rem 0;
            border-top: 1px solid var(--w-border);
            font-size: 0.88rem;
            color: var(--w-text-muted);
            line-height: 1.5;
        }
        .wh-step:first-of-type { border-top: none; padding-top: 0; }
        .wh-step-num {
            flex-shrink: 0;
            width: 24px; height: 24px;
            border-radius: 50%;
            background: var(--w-accent-soft);
            color: var(--w-accent);
            font-weight: 700;
            font-size: 0.76rem;
            display: flex; align-items: center; justify-content: center;
        }
        .wh-step strong { color: var(--w-text); }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _hub_icon_svg():
    """Decorative network/hub graphic echoing the reference screenshot."""
    return """
    <div class="wh-hub-wrap">
        <svg width="170" height="170" viewBox="0 0 170 170" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <linearGradient id="whGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#4f6df5"/>
                    <stop offset="100%" stop-color="#7c5cf0"/>
                </linearGradient>
            </defs>
            <line x1="85" y1="85" x2="30" y2="35" stroke="#dbe2f3" stroke-width="2"/>
            <line x1="85" y1="85" x2="140" y2="35" stroke="#dbe2f3" stroke-width="2"/>
            <line x1="85" y1="85" x2="30" y2="135" stroke="#dbe2f3" stroke-width="2"/>
            <line x1="85" y1="85" x2="140" y2="135" stroke="#dbe2f3" stroke-width="2"/>
            <line x1="85" y1="85" x2="85" y2="20" stroke="#dbe2f3" stroke-width="2"/>
            <line x1="85" y1="85" x2="85" y2="150" stroke="#dbe2f3" stroke-width="2"/>
            <circle cx="85" cy="85" r="30" fill="url(#whGrad)"/>
            <circle cx="85" cy="85" r="30" fill="none" stroke="#ffffff" stroke-width="2" opacity="0.5"/>
            <circle cx="30" cy="35" r="7" fill="#7c5cf0"/>
            <circle cx="140" cy="35" r="7" fill="#4f6df5"/>
            <circle cx="30" cy="135" r="7" fill="#4f6df5"/>
            <circle cx="140" cy="135" r="7" fill="#7c5cf0"/>
            <circle cx="85" cy="20" r="6" fill="#9aa8f7"/>
            <circle cx="85" cy="150" r="6" fill="#9aa8f7"/>
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
    community_prs = "—"

    _inject_welcome_theme()

    st.markdown('<div id="ph-welcome-root">', unsafe_allow_html=True)

    # ---------------- TOP NAV ----------------
    st.markdown(
        """
        <div class="wh-nav wh-fade">
            <div class="wh-nav-left">
                <span class="wh-nav-logo"></span>
                PySource Hub
            </div>
            <div class="wh-nav-links">
                <span>Projects</span>
                <span>Getting Started</span>
                <span>Documentation</span>
                <span>Community</span>
            </div>
            <a class="wh-nav-cta" href="https://github.com/" target="_blank">⭐ Fork us on GitHub</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---------------- STAT GRID + HUB ICON + WELCOME CARD ----------------
    col_stats, col_hub, col_welcome = st.columns([1.15, 0.7, 1.15], gap="medium")

    with col_stats:
        s1, s2 = st.columns(2, gap="small")
        with s1:
            st.markdown(
                f"""
                <div class="wh-stat-card wh-fade wh-d1">
                    <div class="wh-stat-label">Total Active Repos</div>
                    <div class="wh-stat-value">{total_repos}</div>
                    <div class="wh-stat-sub">Catalog modules loaded</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown(
                f"""
                <div class="wh-stat-card wh-fade wh-d3">
                    <div class="wh-stat-label">Patches Merged</div>
                    <div class="wh-stat-value">{patches_merged}</div>
                    <div class="wh-stat-sub">Modules with zero open issues</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with s2:
            st.markdown(
                f"""
                <div class="wh-stat-card wh-fade wh-d2">
                    <div class="wh-stat-label">Community Pull Requests</div>
                    <div class="wh-stat-value">{community_prs}</div>
                    <div class="wh-stat-sub">Pending GitHub API integration</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown(
                f"""
                <div class="wh-stat-card wh-fade wh-d4">
                    <div class="wh-stat-value" style="margin-top:0;">{total_open_challenges}</div>
                    <div class="wh-stat-label" style="margin-top:0.3rem; margin-bottom:0;">Open Challenges</div>
                    <div class="wh-stat-sub">Limitations across all modules</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with col_hub:
        st.markdown(f'<div class="wh-fade wh-d2">{_hub_icon_svg()}</div>', unsafe_allow_html=True)

    with col_welcome:
        st.markdown(
            """
            <div class="wh-welcome-card wh-fade wh-d3">
                <div class="wh-welcome-title">👋 Welcome</div>
                <div class="wh-welcome-text">
                    Welcome to the Micro-CMS / Micro-CMS architecture, with
                    core and interactive elements, code metadata, and
                    metadata-standardized .py files.
                </div>
                <div class="wh-diagram">
                    <div class="wh-diagram-node">
                        <div class="wh-diagram-box">📄</div>
                        .py files
                    </div>
                    <div class="wh-diagram-arrow">→</div>
                    <div class="wh-diagram-node">
                        <div class="wh-diagram-box">🧩</div>
                        Code metadata
                    </div>
                    <div class="wh-diagram-arrow">→</div>
                    <div class="wh-diagram-node">
                        <div class="wh-diagram-box">🖥️</div>
                        UI
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ---------------- MISSION / CONTRIBUTION (kept from prior content) ----------------
    st.markdown('<div class="wh-section-label wh-fade wh-d3">🎯 Core Mission</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="wh-body-card wh-fade wh-d3">
            <div class="wh-body-text">
                <strong>"Read-First, Patch-Second."</strong> Traditional platforms focus
                on competitive coding inside isolated browser sandboxes. PySource Hub is
                engineered to bridge the gap between classroom syntax and professional
                development — students enter an active, production-ready environment to
                study working blueprints, discover documented architectural limitations,
                and submit functional upgrades using real-world Git-Flow workflows.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="wh-section-label wh-fade wh-d4">🤝 The 4-Step Contribution Manual</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="wh-body-card wh-fade wh-d4">
            <div class="wh-step">
                <div class="wh-step-num">1</div>
                <div><strong>Select a Repository</strong> — pick a project from the left sidebar index dropdown.</div>
            </div>
            <div class="wh-step">
                <div class="wh-step-num">2</div>
                <div><strong>Audit Flaws</strong> — analyze the documented bugs or architectural limitations.</div>
            </div>
            <div class="wh-step">
                <div class="wh-step-num">3</div>
                <div><strong>Fork &amp; Code</strong> — link to GitHub, fork the repository, and patch the limitation locally.</div>
            </div>
            <div class="wh-step">
                <div class="wh-step-num">4</div>
                <div><strong>Pull Request</strong> — submit your code review request! Once merged, your optimized logic replaces the blueprint live.</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)  # close #ph-welcome-root