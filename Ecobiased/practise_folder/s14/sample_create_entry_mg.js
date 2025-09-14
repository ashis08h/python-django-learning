define('o9.AddSafetyStockOverride',['o9/data/query', 'o9/data/cellset'],function(){

	var ActionButtonCall = function(o9Params) {

		// Parse the JSON file passed fraom action button
		var parsedParams = JSON.parse(o9Params);

		// Log the values passed from action button
		Log.Info("parsedParams.VersionName ... " +parsedParams.VersionName);
		Log.Info("parsedParams.SKU: " +parsedParams.SKU);
		Log.Info("parsedParams.Store: " +parsedParams.Store);
		Log.Info("parsedParams.StartDate: " +parsedParams.StartDate);
		Log.Info("parsedParams.EndDate: " +parsedParams.EndDate);
		Log.Info("parsedParams.SafetyStockOverride: " +parsedParams.SSOverride);
		Log.Info("parsedParams.OverrideReason: " +parsedParams.OverrideReason);

		// Initialize query modules
		var queryModule = require('o9/data/query');
		var cellsetModule = require('o9/data/cellset');

		/* ----- VALIDATION CONDITION BEGIN ----- */

		// Display prompt if user filled neither of the inputs
		if (parsedParams.SSOverride == null) {
			Log.Info("Raising error for no inputs");
			RuleOutputToUI = {
				Status: 'Error',
				Message: 'Please enter Safety Stock Override number.'
			};
			// Exit if validation failed
			return;
		}

		if (parsedParams.EndDate != null) {

		if (parsedParams.StartDate > parsedParams.EndDate) {
			Log.Info("Raising error for StartDate greater than EndDate");
			RuleOutputToUI = {
				Status: 'Error',
				Message: 'Please enter Start Date smaller than End Date.'
			};
			return;
		}

		}

		/* ----- UPDATE QUERIES BEGIN ----- */
		var i;
		var j;
		for (i in parsedParams.SKU) {
			for (j in parsedParams.Store){
				Log.Info("SKU: " + parsedParams.SKU[i]);
				Log.Info("Store: " + parsedParams.Store[j]);


		if (parsedParams.SSOverride != null) {


		var stdate = parsedParams.StartDate;
		var startdate = stdate.substring(0, 10);


		//checking if parsed End date is null

		if (parsedParams.EndDate != null) {

		Log.Info("Threshold Parsed End Date String: " + parsedParams.EndDate);
		var endate = parsedParams.EndDate;
		var enddate = endate.substring(0, 10);

		// Check for existing overrides with no end date that would conflict
		var noEndDateConflictQuery = 'Select([Version].[Version Name].['+ parsedParams.VersionName +'] * [SCSItem].[Item].filter(#.Name in {"'+ parsedParams.SKU[i] +'"}) * [SCSLocation].[Location].filter(#.Name in {"'+parsedParams.Store[j]+'"}) * [Time].[Day]) on row, ({Measure.[SafetyStock], Measure.[SafetyStockStartDate], Measure.[SafetyStockEndDate]}) on column;';
		Log.Info("No end date conflict validation query: " +JSON.stringify(noEndDateConflictQuery));
		var noEndDateConflictData = cellsetModule.createCellSet(queryModule.select(noEndDateConflictQuery));
		Log.Info("No end date conflict validation data: " +JSON.stringify(noEndDateConflictData));

		// Check the results manually for conflicts
		var hasConflict = false;
		for (var k = 0; k < noEndDateConflictData.rowCount; k++) {
			var row = noEndDateConflictData.row(k);
			var safetyStock = row.cell(0).Value;
			var startDate = row.cell(1).Value;
			var endDate = row.cell(2).Value;

			if (safetyStock != null && startDate != null && endDate == null) {
				var existingStart = new Date(startDate);
				var newEnd = new Date(parsedParams.EndDate);
				if (existingStart <= newEnd) {
					hasConflict = true;
					break;
				}
			}
		}

		if (hasConflict) {
			Log.Info("Raising error for conflict with existing override that has no end date");
			RuleOutputToUI = {
				Status: 'Error',
				Message: 'There is already a Safety Stock Override with no end date that conflicts with this date range. The new override end date must be before the existing override start date.'
			};
			return;
		}

		validationQuery = 'Select([Version].[Version Name].['+ parsedParams.VersionName +'] * [SCSItem].[Item].filter(#.Name in {"'+ parsedParams.SKU[i] +'"})* [SCSLocation].[Location].filter(#.Name in {"'+parsedParams.Store[j]+'"}) * [Time].[Day].filter(#.Key >= TODATETIME("'+ parsedParams.StartDate +'") && #.Key <= TODATETIME("'+ parsedParams.EndDate +'"))) on row, ({Measure.[SafetyStock]}) on column;';
		Log.Info("Safety Stock validation query: " +JSON.stringify(validationQuery));
		validationData = cellsetModule.createCellSet(queryModule.select(validationQuery));  // Execute select query and build cellset
		Log.Info("Safety Stock validation data: " +JSON.stringify(validationData));

		var finalEndDate = parsedParams.EndDate;

		}

		if (parsedParams.EndDate == null) {

		// Check for existing overrides with no end date that would conflict
		var noEndDateValidationQuery = 'Select([Version].[Version Name].['+ parsedParams.VersionName +'] * [SCSItem].[Item].filter(#.Name in {"'+ parsedParams.SKU[i] +'"}) * [SCSLocation].[Location].filter(#.Name in {"'+parsedParams.Store[j]+'"}) * [Time].[Day]) on row, ({Measure.[SafetyStock], Measure.[SafetyStockStartDate], Measure.[SafetyStockEndDate]}) on column;';
		Log.Info("No end date validation query: " +JSON.stringify(noEndDateValidationQuery));
		var noEndDateValidationData = cellsetModule.createCellSet(queryModule.select(noEndDateValidationQuery));
		Log.Info("No end date validation data: " +JSON.stringify(noEndDateValidationData));

		// Check the results manually for existing overrides with no end date
		var hasExistingNoEndDate = false;
		for (var m = 0; m < noEndDateValidationData.rowCount; m++) {
			var row = noEndDateValidationData.row(m);
			var safetyStock = row.cell(0).Value;
			var startDate = row.cell(1).Value;
			var endDate = row.cell(2).Value;

			if (safetyStock != null && startDate != null && endDate == null) {
				hasExistingNoEndDate = true;
				break;
			}
		}

		if (hasExistingNoEndDate) {
			Log.Info("Raising error for conflict with existing override that has no end date");
			RuleOutputToUI = {
				Status: 'Error',
				Message: 'There is already a Safety Stock Override with no end date. Cannot add another override without end date for the same SKU-Store combination.'
			};
			return;
		}

		validationQuery = 'Select([Version].[Version Name].['+ parsedParams.VersionName +'] * [SCSItem].[Item].filter(#.Name in {"'+ parsedParams.SKU[i] +'"}) * [SCSLocation].[Location].filter(#.Name in {"'+parsedParams.Store[j]+'"}) * [Time].[Day].filter(#.Key >= TODATETIME("'+ parsedParams.StartDate +'"))) on row, ({Measure.[SafetyStock]}) on column;';
		Log.Info("Safety Stock validation query: " +JSON.stringify(validationQuery));
		validationData = cellsetModule.createCellSet(queryModule.select(validationQuery));  // Execute select query and build cellset
		Log.Info("Safety Stock validation data: " +JSON.stringify(validationData));

		Log.Info("Threshold Parsed End Date is null ");
		var enddate = null;
		var finalEndDate = null;
		}



		//item startdate query
		isdquery = 'Select ({Measure.[StartDate]}) where {[Version].[Version Name].['+ parsedParams.VersionName +'], [SCSItem].[Item].filter(#.Name in {"'+ parsedParams.SKU[i] +'"}), [SCSLocation].[Location].filter(#.Name in {"'+ parsedParams.Store[j]+'"})};';

		isdquery1 = queryModule.select(isdquery);

		isdquery2 =  Object.keys(isdquery1).map(function(key) {return isdquery1[key];});
		isdqueryv = isdquery2[1]

		Log.Info("Item Start Date: " + isdqueryv);

		var start1 = JSON.stringify(isdqueryv);

		Log.Info("Item Start Date String: " + start1);

		if (start1 == "[]")
		{
		Log.Info("Item start date is null" );
		}

		if (start1 != "[]")
		{
		Log.Info("Item start date is not null " + start1 );
		}


		//checking for item start date smaller or greater than param start date
		if (isdqueryv < parsedParams.StartDate)
		{

		var final_start = parsedParams.StartDate
		Log.Info("Item startdate is less than param start date" );
		Log.Info("Final startdate is:" + final_start );

		} else {

		var final_start = isdqueryv
		var a = start1.substring(4,23)
		Log.Info("Final startdate A:" + a );
		final_start = a
		Log.Info("Item startdate is greater than param start date" );
		Log.Info("Final startdate is:" + final_start );

		}


		if (validationData.rowCount > 0) {

			if (parsedParams.EndDate == null) {
			Log.Info("Raising error for Overlap in Safety Stock Override");
			RuleOutputToUI = {
				Status: 'Error',
				Message: 'There is already an Safety Stock Overide value defined from '+ startdate +' with no end date'
			};
			} else {
			Log.Info("Raising error for Overlap in Safety Stock Override");
			RuleOutputToUI = {
				Status: 'Error',
				Message: 'There is already an Safety Stock Overide value defined between '+ startdate +'  and '+ enddate +''
			};
			}
			return;
		}

		if (validationData.rowCount <= 0) {
			// Update with Safety Stock override
			var query;
			if (finalEndDate != null) {
				query = 'cartesian scope:([Version].[Version Name].['+ parsedParams.VersionName +'] * [SCSItem].[Item].filter(#.Name in {"'+  parsedParams.SKU[i] +'"}) * [SCSLocation].[Location].filter(#.Name in {"'+ parsedParams.Store[j]+'"}) * [Time].[Day].filter(#.Key >= TODATETIME("'+ final_start +'") && #.Key <= TODATETIME("'+ finalEndDate +'"))); Measure.[SafetyStock] = if(isnull(Measure.[SafetyStock])) then "'+ parsedParams.SSOverride +'"; end scope;';
			} else {
				query = 'cartesian scope:([Version].[Version Name].['+ parsedParams.VersionName +'] * [SCSItem].[Item].filter(#.Name in {"'+  parsedParams.SKU[i] +'"}) * [SCSLocation].[Location].filter(#.Name in {"'+ parsedParams.Store[j]+'"}) * [Time].[Day].filter(#.Key >= TODATETIME("'+ final_start +'"))); Measure.[SafetyStock] = if(isnull(Measure.[SafetyStock])) then "'+ parsedParams.SSOverride +'"; end scope;';
			}
			queryModule.update(query);
		}


		}

		// Update override reason code & End Date
		if (parsedParams.EndDate == null){
		var query = 'cartesian scope:([Version].[Version Name].['+ parsedParams.VersionName +'] * [SCSItem].[Item].filter(#.Name in {"'+  parsedParams.SKU[i] +'"}) * [SCSLocation].[Location].filter(#.Name in {"'+ parsedParams.Store[j]+'"}) * [Time].[Day].filter(#.Key == TODATETIME("'+ final_start +'"))); Measure.[SafetyStockStartDate] = "'+ final_start +'"; Measure.[SafetyStockEndDate] = null; Measure.[SafetyStockOverrideReason] = "'+ parsedParams.OverrideReason +'"; end scope;';
		queryModule.update(query);
		} else {
		var query = 'cartesian scope:([Version].[Version Name].['+ parsedParams.VersionName +'] * [SCSItem].[Item].filter(#.Name in {"'+  parsedParams.SKU[i] +'"}) * [SCSLocation].[Location].filter(#.Name in {"'+ parsedParams.Store[j]+'"}) * [Time].[Day].filter(#.Key == TODATETIME("'+ final_start +'")));Measure.[SafetyStockStartDate] = "'+ final_start +'"; Measure.[SafetyStockEndDate] = "'+ finalEndDate +'"; Measure.[SafetyStockOverrideReason] = "'+ parsedParams.OverrideReason +'"; end scope;';
		queryModule.update(query);
		}



		}
	}
		/* ----- UPDATE QUERIES END ----- */

	};

	var ConcatenateMultiselect = function(value){

		if (Array.isArray(value)) {
			var test = value.join('","');
			return test;
		}
		return value;

	};

	return {

	  ActionButtonCall:ActionButtonCall

	};

});