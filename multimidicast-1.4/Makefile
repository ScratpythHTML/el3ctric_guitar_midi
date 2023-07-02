# $Header: /home/doj/code/multimidicast/Makefile,v 1.2 2007-10-22 17:57:03 doj Exp $

CXXFLAGS+=-Wall -O2 -std=c++11
LIBS+=-lasound
PREFIX?=$(DESTDIR)/usr

multimidicast:	multimidicast.o
	$(CXX) $(LDFLAGS) -o $@ $^ $(LIBS)

install:	multimidicast
	install -m 755 multimidicast $(PREFIX)/bin/

uninstall:
	$(RM) $(PREFIX)/bin/multimidicast

clean:
	$(RM) multimidicast *.o *~
