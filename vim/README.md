# vim

A minimal Vim setup: one `vimrc`, two colorschemes, one optional plugin (fzf).
The point is muscle memory that works anywhere — on a new machine, paste the
`vimrc`; the themes and fzf are optional, and without fzf the search keys fall
back to Vim's own `:find`/`:grep`.

This replaces the old 2018 `vimconfig` bundle setup and merges the settings of
the previous live `~/.vimrc` (light background, clipboard, persistent undo).

## Install

    make install      # ~/.vimrc + ~/.vim/colors/ + fzf plugins (only if fzf exists)

`fzf` itself must be installed separately (`apt install fzf`). `make install`
then clones **both** fzf Vim repositories, because `fzf.vim` (the commands) needs
the base plugin from the fzf repository (it provides `fzf#run()`):

    ~/.vim/pack/utils/opt/fzf       <- junegunn/fzf       (base plugin)
    ~/.vim/pack/utils/opt/fzf-vim   <- junegunn/fzf.vim   (:Files, :Rg, ...)

An existing `~/.vimrc` is backed up once to `~/.vimrc.bak`. In Vim: `:Erc`
edits the config, `:Lrc` reloads it.

## All mappings (leader is space)

| key | action |
|---|---|
| `<space>p` | pick a file: fzf `:Files`, or `:find` without fzf |
| `<space>g` | search text: fzf `:Rg`, or `:grep` without fzf (opens quickfix) |
| `<C-p>` | same as `<space>p` (only when fzf is installed) |
| `<space>f` | move to the split on the left (`<C-w>h`) |
| `<space>j` | move to the split on the right (`<C-w>l`) |
| `<space>n` | file browser (netrw `:Lexplore`, no banner) |
| `<space>b` | buffer list (`:ls`), then type the number |
| `<space>#` | previous buffer (`:b #`) |
| `<space>s` | vertical split |
| `<space>w` | strip trailing whitespace and save |
| `<C-j>` / `<C-k>` | 5 lines down / up |
| `<CR>` | clear search highlight |
| `>` / `<` (visual) | indent / outdent, keep selection |

## Commands

| command | action |
|---|---|
| `:Erc` / `:Lrc` | edit / reload `$MYVIMRC` |
| `:Rts` | strip trailing whitespace |
| `:Lexplore` | file browser (netrw) |
| `:copen` / `:cnext` / `:cprev` | quickfix list, e.g. after `:grep` |
| `:Files`, `:GFiles`, `:Buffers`, `:History`, `:Lines`, `:BLines`, `:Rg`, `:Marks` | fzf pickers (when installed) |

## Searching: what does what

- `/pattern` — Vim's own search in the current buffer. `ignorecase`+`smartcase`
  (all lower-case = case-insensitive, any capital = exact), `n`/`N` repeat,
  `<CR>` clears the highlight, `*`/`#` search the word under the cursor.
- `<space>p` / `<C-p>` — **file names**. With fzf: fuzzy picker over the working
  directory; type a few letters, Enter opens, `<C-v>`/`<C-x>`/`<C-t>` open in a
  split/tab, `<Tab>` marks several. Without fzf: `:find` + `<Tab>` completion
  over the whole tree (`path+=**`), no fuzzy matching.
- `<space>g` — **text content**. With fzf: `:Rg` (ripgrep, live results while you
  type, `--smart-case`; Enter jumps to the match). Without fzf: `:grep` fills the
  quickfix list and opens it automatically; `:cnext`/`:cprev` walk the hits.
- `<space>n` — browse directories instead of searching: Enter opens, `-` goes
  up, `R` rename, `d`/`%` new directory/file, `D` delete, `gh` hidden files.
- `<space>b` / `<space>#` — switch between files that are already open. With
  fzf, `:Buffers` is the fuzzy version of that.

## Themes

`catppuccin_latte` (light, default) and `catppuccin_mocha` (dark) are vendored
from https://github.com/catppuccin/vim (MIT):

    :colorscheme catppuccin_mocha

Any other single-file colorscheme can be dropped into `colors/` and installed
with `make install`. If none is found (remote paste without themes), the
`vimrc` falls back to `peachpuff`.

Settings: 4-space expandtab + smartindent, number, cursorline, colored area past
column 80, trailing-whitespace highlight, `hidden`, mouse, clipboard,
`ignorecase smartcase`, 2-line statusline, persistent undo and backups under
`~/.vim/`, `ttimeoutlen=10` for a fast Esc. The rest comes from
`$VIMRUNTIME/defaults.vim` (Vim's own recommended defaults).

Note: `[No Name]` in `:ls` is Vim's normal start buffer when Vim is opened
without a file; delete it with `:bw` if it bothers you. Netrw's own directory
buffers are unlisted (`nobl`) and wiped when the explorer closes.

## No plugins needed for

netrw for file browsing, `:find` for files, ripgrep via `:grep` + quickfix,
`:terminal` for git, hand-rolled statusline, `match` for whitespace. fzf.vim
plus its base plugin (both MIT: https://github.com/junegunn/fzf.vim,
https://github.com/junegunn/fzf) are the only exception.
