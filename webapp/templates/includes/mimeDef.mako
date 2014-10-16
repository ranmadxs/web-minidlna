<%def name="showMime(mediaFile, type='regular')">
	% if mediaFile!=None:
    	account name: ${mediaFile}, type: ${type}
	% endif    
</%def>