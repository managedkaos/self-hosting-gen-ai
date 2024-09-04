README_FILES := $(shell find . -type f -name 'README.md' -not -path './.git/*')

info:
	echo "This makefile is used to maintain this repository. It is not intended to be used by the end user."

all: pull-external-content lint spellcheck
	@echo "Done."

lint:
	-@docker pull ghcr.io/managedkaos/summarize-markdown-lint:main
	-@docker pull davidanson/markdownlint-cli2:v0.13.0
	-@docker run -v $(PWD):/workdir davidanson/markdownlint-cli2:v0.13.0 $(README_FILES) 2>&1 | \
		docker run --interactive ghcr.io/managedkaos/summarize-markdown-lint:main

rawlint:
	-@docker run -v $(PWD):/workdir davidanson/markdownlint-cli2:v0.13.0 $(README_FILES) 2>&1

spellcheck:
	@echo "Spell checking README files..."
	@for file in $(README_FILES); do \
		echo "\t$$file"; \
		aspell check --mode=markdown --lang=en $$file; \
	done

pull-external-content: 0-laptop-ollama-openwebui 1-cloud-ollama-openwebui

0-laptop-ollama-openwebui:
	cp -v ../ollama-mgmt/README.md ./0-laptop-ollama-openwebui
	cp -v ../ollama-mgmt/Makefile ./0-laptop-ollama-openwebui
	cp -v ../ollama-mgmt/*.txt ./0-laptop-ollama-openwebui
	cp -v ../ollama-mgmt/*.py ./0-laptop-ollama-openwebui

1-cloud-ollama-openwebui:
	cp -v ../ollama-cloudformation/README.md ./1-cloud-ollama-openwebui
	cp -v ../ollama-cloudformation/Makefile ./1-cloud-ollama-openwebui
	cp -v ../ollama-cloudformation/*.yml ./1-cloud-ollama-openwebui

.PHONY: all lint rawlint info pull-external-content 0-laptop-ollama-openwebui 1-cloud-ollama-openwebui
