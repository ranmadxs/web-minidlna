<%inherit file="layout/base.mako"/>

<%block name="content">
    <h3>minidlna.conf file</h3><br />
    <b>File Config:</b> ${model['dlnaFileConfig']} <br />
    <b>DB Dir:</b> ${model['db_dir']} <br />
    <br /><u>Directory List</u> (Type , Path) <br />
    <ul>
		% for mediaDir in listMediaDir:
  			<li>${mediaDir.tipo} , ${mediaDir.path}</li>
		% endfor
	</ul>
    
</%block>