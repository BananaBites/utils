.PHONY: install

install:
	mkdir -p ~/.utils/bin ~/.config/tmux
	install -m 755 tls ~/.utils/bin/tls
	install -m 644 tmux.conf ~/.config/tmux/tmux.conf
	@echo 'Add this to your shell profile:  export PATH="$$HOME/.utils/bin:$$PATH"'

