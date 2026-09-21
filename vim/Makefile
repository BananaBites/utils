VIMDIR ?= $(HOME)/.vim
FZF := $(VIMDIR)/pack/utils/opt/fzf
FZF_VIM := $(VIMDIR)/pack/utils/opt/fzf-vim

.PHONY: install

install:
	mkdir -p $(VIMDIR)/colors $(VIMDIR)/pack/utils/opt
	@if [ -f $(HOME)/.vimrc ] && [ ! -f $(HOME)/.vimrc.bak ]; then cp $(HOME)/.vimrc $(HOME)/.vimrc.bak; fi
	cp vimrc $(HOME)/.vimrc
	cp colors/*.vim $(VIMDIR)/colors/
	@if command -v fzf >/dev/null; then \
		[ -f $(FZF)/install ] || { rm -rf $(FZF); git clone --depth 1 https://github.com/junegunn/fzf $(FZF); }; \
		[ -d $(FZF_VIM) ] || git clone --depth 1 https://github.com/junegunn/fzf.vim $(FZF_VIM); \
	fi

