<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>How to Read CSV file and Display its content using JavaScript</title>
</head>
<body>
	<!-- CSS -->
	<style type="text/css">
		table th, table td{
			padding: 5px;
		}
	</style>

	<div>

		<div>
			<input type="file" name="file" id="file" accept=".csv"  > <br><br>
			<input type="button" id="btnsubmit" value="Submit" onclick="readCSVFile();" >
		</div>

		<br><br>
		<!-- List CSV file data -->
		<table id="tblcsvdata" border="1" style="border-collapse: collapse;">
			<thead>
				<tr>
					<th>S.no</th>
					<th>Username</th>
					<th>Name</th>
					<th>Email</th>
				</tr>
			</thead>
			<tbody>
				
			</tbody>

		</table>
	</div>

	<!-- Script -->
	<script type="text/javascript">

	function readCSVFile(){
		var files = document.querySelector('#file').files;

		if(files.length > 0 ){

			// Selected file
			var file = files[0];

			// FileReader Object
	  		var reader = new FileReader();

	  		// Read file data as string	
	  		reader.readAsText(file);

	  		// Load event
	  		reader.onload = function(event) {
		           	
		        // Read file data
				var csvdata = event.target.result;

				// Split by line break to gets rows Array
				var rowData = csvdata.split('\n');

				// <table > <tbody>
				var tbodyEl = document.getElementById('tblcsvdata').getElementsByTagName('tbody')[0];
				tbodyEl.innerHTML = "";

				// Loop on the row Array (change row=0 if you also want to read 1st row)
				for (var row = 1; row < rowData.length; row++) {

				   	// Insert a row at the end of table
					var newRow = tbodyEl.insertRow();

				    // Split by comma (,) to get column Array
				    rowColData = rowData[row].split(',');
				      	
				    // Loop on the row column Array
				    for (var col = 0; col < rowColData.length; col++) {

				      	// Insert a cell at the end of the row
						var newCell = newRow.insertCell();
				        newCell.innerHTML = rowColData[col];

				    }
				      	
				}
		    };
		    
		}else{
			alert("Please select a file.");
		}
  		
	}
	
	</script>
</body>
</html>