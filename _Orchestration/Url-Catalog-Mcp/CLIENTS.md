# How to connect the URL catalog (for humans)

**Owning seat:** Master (Tim)  
**Status:** Live. 2026-08-17.

You do not need to know what MCP or sqlite are.

- **Apps on this Mac that support MCP** can **search** the catalog and **add** URLs.
- **ChatGPT / Claude in a web browser** can only **read** the last published copy. They cannot add URLs.
- **Ollama by itself** cannot connect. It only runs models. Put the catalog on LM Studio, AnythingLLM, Cursor, or VS Code, and let those apps talk to Ollama if you want a local model.

Cursor is already connected. ChatGPT in the browser is already pointed at the published JSON.

Do **not** publish GitHub Pages unless you decided to. Do **not** delete files. If a JSON paste looks wrong, stop and tell Cursor.

---

## Your apps (this Mac)

| App | Can it connect? | What you do |
|---|---|---|
| **Cursor Desktop** | Yes. Already on. | Use it. Search for cryptids. |
| **Claude Desktop** | Yes. You paste a config. | Section 2. |
| **Antigravity Desktop** | Yes. | Section 3. |
| **Antigravity IDE** | Yes. Same catalog file as Desktop. | Section 3. |
| **VS Code** | Yes. Slightly different JSON key (`servers`). | Section 4. |
| **LM Studio** | Yes. | Section 5. |
| **AnythingLLM** | Yes. Must use **@agent**. | Section 6. |
| **Ollama** | No. Model engine only. | Section 7. |
| **ChatGPT in a browser** | Read-only URL. Already done. | Section 8. |

After each desktop app: new chat, type `Search my URL catalog for cryptids.` You should see real links (Cryptid Vault, and so on). If it invents sites, it is not connected.

---

## The catalog program (copy this path exactly)

```
python3
```

```
/Volumes/FLEET-01/FLEET-01/Websites/url-catalog/_Orchestration/Url-Catalog-Mcp/server.py
```

Do not point anything at Research-Sandbox.

---

## 1. Cursor Desktop — already done

Skip unless tools vanish.

**Settings → MCP → url-catalog** → reload, or quit Cursor (`Cmd + Q`) and open it again.

---

## 2. Claude Desktop — do this first if you have not

This is the Claude **app**, not claude.ai in Safari.

1. Quit Claude fully: Claude menu → **Quit Claude**.
2. Finder → **Go** → **Go to Folder…** (`Shift + Cmd + G`).
3. Paste this and press Go:

```
~/Library/Application Support/Claude/
```

4. Look for `claude_desktop_config.json`.

**If the file does not exist:** TextEdit → Format → **Make Plain Text**. Paste this whole box. Save as `claude_desktop_config.json` in that folder (not `.txt`).

```json
{
  "mcpServers": {
    "url-catalog": {
      "command": "python3",
      "args": [
        "/Volumes/FLEET-01/FLEET-01/Websites/url-catalog/_Orchestration/Url-Catalog-Mcp/server.py"
      ]
    }
  }
}
```

**If the file already has stuff in it:** do not wipe it. Inside `"mcpServers": { ... }`, add a comma after the last server, then paste only:

```json
    "url-catalog": {
      "command": "python3",
      "args": [
        "/Volumes/FLEET-01/FLEET-01/Websites/url-catalog/_Orchestration/Url-Catalog-Mcp/server.py"
      ]
    }
```

5. Open Claude Desktop. New chat. Type: `Search my URL catalog for cryptids.`

Easier path that also creates the file: Claude menu (top bar, not inside the window) → **Settings…** → **Developer** → **Edit Config**, then paste as above, save, quit, reopen.

If it fails: stop. Do not keep editing commas. Tell Cursor.

---

## 3. Antigravity Desktop and Antigravity IDE

Same catalog. Two ways in. Custom server (ours) is **not** in Google’s MCP Store, so you paste config.

### Antigravity Desktop (2.0)

1. Open Antigravity Desktop.
2. **Settings** (bottom left) → **Customizations** → **Installed MCP Servers**.
3. If you only see a Store: you still need the raw file. Continue with “the JSON file” below.

### Antigravity IDE

1. Open Antigravity IDE.
2. In the **agent side panel**, click **…** (top) → **MCP Servers**.
3. **Manage MCP Servers** → **View raw config**.

### The JSON file (both)

Finder → Go to Folder:

```
~/.gemini/config/
```

File: `mcp_config.json`

If missing, create it (plain text) with the **full** box:

```json
{
  "mcpServers": {
    "url-catalog": {
      "command": "python3",
      "args": [
        "/Volumes/FLEET-01/FLEET-01/Websites/url-catalog/_Orchestration/Url-Catalog-Mcp/server.py"
      ]
    }
  }
}
```

If it already has servers, insert the `url-catalog` block inside `mcpServers` (comma after the previous one). Save. Restart Antigravity. New chat. Cryptids test.

Optional workspace-only copy (only that project): `.agents/mcp_config.json` inside the project. Prefer the global file so every Antigravity window sees the catalog.

---

## 4. VS Code

VS Code uses `"servers"`, not `"mcpServers"`. Copy the VS Code box, not the Claude box.

**Easiest:**

1. Open VS Code.
2. `Cmd + Shift + P` → type `MCP: Add Server` → Return.
3. Choose **stdio** / command.
4. Command: `python3`
5. Arguments: `/Volumes/FLEET-01/FLEET-01/Websites/url-catalog/_Orchestration/Url-Catalog-Mcp/server.py`
6. Name: `url-catalog`
7. Choose **Global** (all workspaces), not only this folder.
8. Trust / start the server when asked.
9. Open Chat (`Ctrl + Cmd + I`). New chat. Cryptids test.

**If you prefer a file:** `Cmd + Shift + P` → `MCP: Open User Configuration`. Paste:

```json
{
  "servers": {
    "url-catalog": {
      "type": "stdio",
      "command": "python3",
      "args": [
        "/Volumes/FLEET-01/FLEET-01/Websites/url-catalog/_Orchestration/Url-Catalog-Mcp/server.py"
      ]
    }
  }
}
```

If that file already has `"servers"`, only add the `url-catalog` object (with a comma). Then `Cmd + Shift + P` → **Reload Window**.

---

## 5. LM Studio

1. Open LM Studio.
2. Right-hand sidebar → **Program** tab.
3. **Install** → **Edit mcp.json**.
4. LM Studio follows Cursor-style JSON. If the file is empty, paste the **full Claude/Cursor box** (`mcpServers`). If it already has servers, paste only the `url-catalog` object inside `mcpServers`.
5. Save. Make sure the server is **on**.
6. Chat with a model that is allowed to use tools. Cryptids test.

Official notes: https://lmstudio.ai/docs/app/mcp

---

## 6. AnythingLLM

You must be on **v1.8.0 or newer**. Tools run as **Agent Skills**. A normal chat often will **not** call MCP until you use `@agent`.

1. Open AnythingLLM.
2. Open **Agent Skills** (sidebar / settings — wording is “Agent Skills”).
   That creates the config file if it was missing.
3. Finder → Go to Folder:

```
~/Library/Application Support/anythingllm-desktop/storage/plugins/
```

4. File: `anythingllm_mcp_servers.json`
5. Paste the **full** `mcpServers` box (same as Claude Desktop) if empty, or insert `url-catalog` if not.
6. Back in AnythingLLM, on Agent Skills, click **Refresh**.
7. Confirm **url-catalog** is running and shows tools (`search_urls`, and so on). If it is stopped, Start it (gear).
8. In a workspace chat, type `@agent` then: `Search my URL catalog for cryptids.`

If a small local model ignores tools, that is the model, not the catalog. Try a larger model.

---

## 7. Ollama — cannot take this wire

Ollama is the engine that **runs** a model. It has no “paste MCP server” box.

What you do instead:

1. Keep Ollama running if you use local models.
2. In **LM Studio**, **AnythingLLM**, **Cursor**, or **VS Code**, pick an Ollama model **and** connect the catalog in **that** app (sections above).

Do not invent a REST API for Ollama.

---

## 8. ChatGPT in a browser — already done, read-only

It uses https://tk-sites.github.io/url-launcher/urls.json  
That is the last **published** snapshot. It cannot add URLs.

---

## Adding a URL (desktop MCP apps only)

> Add this URL to the catalog under Cryptids: https://example.com — one-line what it is.

The app should use **add_drop**. After a batch, ask it to **rebuild_index once**. Do not ask it to push Pages unless you want the public site updated.

---

## If you get stuck

- Missing comma / brace → stop. Tell Cursor the exact file path.
- App has no MCP menu → that app cannot connect. Use Cursor or the browser URL.
- Want Cursor to paste the file for you → name the exact path (for example `~/Library/Application Support/Claude/claude_desktop_config.json`).
