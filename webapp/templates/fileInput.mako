<%inherit file="layout/base.mako"/>

<%block name="menuItem">
	<li><a href="/cgi-bin/webdlna/index.py">Home</a></li>
	<li class="current_page_item"><a href="#">File Input</a></li> 
</%block>

<%block name="content">	
    <h3>File Input</h3><br />
    <form method="post" name="formBuscar" id="formBuscar">
	    <select id="mediaDir" name="mediaDir">
	    	<option value="">Seleccione...</option>
	    	% for mediaDir in listMediaDir:
	  			<option value="${mediaDir.path}" 
	  				% if mediaDir.path==model['mediaDir']:
    					selected
					% endif
	  			>
	  				${mediaDir.tipo} , ${mediaDir.path}/
	  			</option>
			% endfor
		</select>
		<input type="text" name="file" id="file" value="${model['file']}" />
		<input type="submit" name="buscar" id="buscar" value="Buscar" />
		<br />
		<%include file='includes/mimeFile.mako'/>
	</form>    
</%block>