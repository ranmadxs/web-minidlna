<html>
<%include file='head.mako'/>
<body>
<div id="wrapper">
	<div id="header-wrapper">
		<div id="header" class="container">		
			<div id="logo">
				<h1><a href="#">WebDlna</a></h1>
			</div>			
			<div id="menu">
				<ul>
				<%block name="menuItem">
					<li class="current_page_item"><a href="#">Home</a></li>
					<li><a href="#">Acerca de</a></li>
				</%block>
				</ul>
			</div>			
		</div>
		<div id="banner">
			<div class="content"><img src="/cgi-bin/webdlna/webapp/images/img02.jpg" width="1000" height="300" alt="" /></div>
		</div>
	</div>
	<!-- end #header -->
	
	<div id="page">
		<div id="content">
		<%block name="content">
			<div class="post">
				Sin contenido
			</div>
			<div style="clear: both;">&nbsp;</div>
		</%block>
		</div>
		<!-- end #content -->
		<div id="sidebar">
			<ul>
				<li>
					<h2>Categorías</h2>
					<ul>
						<li><a href="#">Manual input</a></li>
						<li><a href="/cgi-bin/webdlna/pages/fileInput.py">File input</a></li>
						<li><a href="#">Daily Scann</a></li>
						<li><a href="#">Last Update</a></li>
						<li><a href="#">Force Reload</a></li>
					</ul>
				</li>
			</ul>
		</div>
		<!-- end #sidebar -->
		<div style="clear: both;">&nbsp;</div>
	</div>
	<!-- end #page --> 
</div>
<div id="footer">
	<%block name="footer">
		<p>Copyright (c) 2013. All rights reserved. Design by <a href="mailto:ranmadxs" rel="nofollow">ranmadxs</a>.</p>
	</%block>
</div>
<!-- end #footer -->
</body>
</html>
