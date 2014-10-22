'''
        Align text columns by given column delimiter.

        A Script for Notepad++ Python Script Plugin.

        @author Dumitru Uzun (DUzun.Me)
        @license MIT
        @version 1.0.0
'''

if not 'alignColumnDelimiter' in globals():
    alignColumnDelimiter = '='

delim = notepad.prompt('Input the column delimiter:', 'Align Columns delimiter string', alignColumnDelimiter);

if delim != None:
    alignColumnDelimiter = delim


def alignColumns():
    (startLine, endLine) = editor.getUserLineSelection();
    caretPos = editor.getCurrentPos();
    modified = 0

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
        i = 0;
        for c in cols:
            l = len(c);
            if i >= len(colWidths):
                colWidths.append(l);
            elif l > colWidths[i]:
                colWidths[i] = l;
            i += 1;
        # endfor
    # endfor

    ''' Align the columns '''
    for ln in range(startLine, endLine+1):
        line = editor.getLine(ln).rstrip();
        cols = line.split(delim);   ''' tabs have already been replaced at this point '''
        lc = len(cols);
        if lc < 2: continue; ''' Ignore lines that do not contain delimiter '''
        chg = 0;
        for i in range(0,lc-1):
            dif = colWidths[i] - len(cols[i]);
            if dif > 0:
                cols[i] += ' ' * dif;
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
