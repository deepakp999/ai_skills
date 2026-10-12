# AI Skills

Agent skills for Claude (Claude.ai, Claude Code, Claude Agent SDK) and other agents that support the `SKILL.md` format.

## Skills

| Skill | What it does |
|---|---|
| [product-design-development](skills/product-design-development/SKILL.md) | Guides any product (physical, digital, service, AI) from opportunity → customer needs → specs → concepts → selection → testing → architecture → prototyping → economics → project plan, with templates and matrices at each stage. Based on the method in *Product Design and Development* by Ulrich, Eppinger & Yang. |

## Installing a skill

**Claude.ai / desktop app:** zip the skill folder (e.g. `product-design-development/`) and upload it under Settings → Capabilities → Skills.

**Claude Code:** copy the folder into `~/.claude/skills/` (personal) or `.claude/skills/` in a project:

```bash
git clone https://github.com/deepakp999/ai_skills
cp -r ai_skills/skills/product-design-development ~/.claude/skills/
```

## Notes

Skill content summarises published methods in original wording; it does not reproduce the source books. Buy the books — they are worth it.
