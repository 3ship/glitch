.PHONY: install
PREFIX = /usr

install:
	install -d "${DESTDIR}${PREFIX}/bin"
	install -m 755 gnitch/gnitch.py "${DESTDIR}${PREFIX}/bin/gnitch"
	install -d "${DESTDIR}${PREFIX}/share/man/man1"
	install -m 644 docs/gnitch.1 "${DESTDIR}${PREFIX}/share/man/man1/gnitch.1"
