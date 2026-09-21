# vim

A minimal Vim setup: one `vimrc`, two colorschemes, one optional plugin (fzf).
The point is muscle memory that works anywhere — on a new machine, paste the
`vimrc`; the themes and fzf are optional and their keys simply stay inactive.

This replaces the old 2018 `vimconfig` bundle setup and merges the settings of
the previous live `~/.vimrc` (light background, clipboard, persistent undo).

## Install

    make install      # ~/.vimrc + ~/.vim/colors/ + fzf.vim (only if fzf exists)

An existing `~/.vimrc` is backed up once to `~/.vimrc.bak`. In Vim: `:Erc`
edits the config, `:Lrc` reloads it, `:Rts` strips trailing whitespace (also on
`<space>w`, which then saves).

## Keys (leader is space)

| key | action |
|---|---|
| `<C-p>` | fzf: files (`:Files`) |
| `<space>f` | `:find`, completes over the tree (`path+=**`) |
| `<space>/` | fzf: live grep (`:Rg`); plain `:grep` without fzf |
| `<space>n` | file browser (netrw `:Lexplore`, no banner; its buffer is wiped when closed) |
| `<space>b` | buffer list, then type the number |
| `<space>s` | vertical split |
| `<space>#` | previous buffer |
| `<space>w` | strip trailing whitespace and save |
| `<C-j>` / `<C-k>` | 5 lines down / up |
| `<CR>` | clear search highlight |
| `>` / `<` (visual) | indent / outdent, keep selection |

Settings: 4-space expandtab + smartindent, number, cursorline, colored area past
column 80, trailing-whitespace highlight, `hidden`, mouse, clipboard,
`ignorecase smartcase`, 2-line statusline, persistent undo and backups under
`~/.vim/`, `ttimeoutlen=10` for a fast Esc. The rest comes from
`$VIMRUNTIME/defaults.vim` (Vim's own recommended defaults).

Note: `[No Name]` in `:ls` is Vim's normal start buffer when Vim is opened
without a file; delete it with `:bw` if it bothers you. Netrw's own directory
buffers are unlisted (`nobl`) and wiped when the explorer closes.

## Themes

`catppuccin_latte` (light, default) and `catppuccin_mocha` (dark) are vendored
from https://github.com/catppuccin/vim (MIT):

    :colorscheme catppuccin_mocha

Any other single-file colorscheme can be dropped into `colors/` and installed
with `make install`. If none is found (remote paste without themes), the
`vimrc` falls back to `peachpuff`.

## No plugins needed for

netrw for file browsing, `:find` for files, ripgrep via `:grep` + quickfix,
`:terminal` for git, hand-rolled statusline, `match` for whitespace. fzf.vim
(MIT, https://github.com/junegunn/fzf.vim) is the only exception.
