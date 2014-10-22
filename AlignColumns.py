'''
    Align text columns by given column delimiter.

    A Script for Notepad++ Python Script Plugin.

    @author Dumitru Uzun (DUzun.Me)
    @license MIT
    @version 1.0.1
'''

if not 'alignColumnDelimiter' in globals():
    alignColumnDelimiter = u'='

delim = notepad.prompt('Input the column delimiter:', 'Align Columns delimiter string', alignColumnDelimiter);

if delim != None:
    alignColumnDelimiter = delim

def utf8len(s):
    r = 0;
    for c in s: r += (ord(c) & 0xC0) != 0xC0; ''' Don't count sync bytes '''
    return r;
# end utf8len()

def alignColumns():
    (startLine, endLine) = editor.getUserLineSelection();
    caretPos = editor.getCurrentPos();
    modified = 0;

    if editor.getCodePage() == 65001:
        charLen = utf8len;
    else:
        charLen = len;
    # endif

    ''' Compute the column widths from all the selected lines '''
    colWidths = []; # colWidths
    for ln in range(startLine, endLine+1):
        i = editor.getLine(ln).rstrip(); ''' ignore trailing spaces '''

        ''' Replace each tab with 4 spaces '''
        line = i.replace("\t", '    ');
        if line != i:
            editor.replaceLine(ln, line);
            modified += 1;
        # endif

        ''' Split line into columns '''
        cols = line.split(delim);
        lc = len(cols);
        if lc < 2: continue; ''' Ignore lines that do not contain delimiter '''
        for i in range(0,lc):
            l = charLen(cols[i]);
            if i >= len(colWidths):
                colWidths.append(l);
            elif l > colWidths[i]:
                colWidths[i] = l;
        # endfor
    # endfor

    c = [];
    for i in colWidths: c.append(str(i));
    v = ":".join(c);

    ''' Align the columns '''
    for ln in range(startLine, endLine+1):
        line = editor.getLine(ln).rstrip();
        cols = line.split(delim);   ''' tabs have already been replaced at this point '''
        lc = len(cols);
        if lc < 2: continue; ''' Ignore lines that do not contain delimiter '''
        chg = 0;
        for i in range(0,lc-1):
            c = cols[i];
            dif = colWidths[i] - charLen(c);
            if dif > 0:
                cols[i] = c + " " * dif;
                chg = 1;
            # endif
        # endfor
        if chg:
            line = delim.join(cols);
            editor.replaceLine(ln, line);
            modified += 1
        # endif
    # endfor

    if modified:
        editor.setEmptySelection(caretPos);
    # endif

# end of alignColumns()

if delim != None:
    ''' First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script '''
    editor.beginUndoAction();

    alignColumns();

    ''' End the undo action, so Ctrl-Z will undo the above two actions '''
    editor.endUndoAction();
# endif
