VIMDIR ?= $(HOME)/.vim
FZF := $(VIMDIR)/pack/utils/opt/fzf

.PHONY: install

install:
	mkdir -p $(VIMDIR)/colors $(VIMDIR)/pack/utils/opt
	@if [ -f $(HOME)/.vimrc ] && [ ! -f $(HOME)/.vimrc.bak ]; then cp $(HOME)/.vimrc $(HOME)/.vimrc.bak; fi
	cp vimrc $(HOME)/.vimrc
	cp colors/*.vim $(VIMDIR)/colors/
	@if command -v fzf >/dev/null && [ ! -d $(FZF) ]; then \
		git clone --depth 1 https://github.com/junegunn/fzf.vim $(FZF); fi

