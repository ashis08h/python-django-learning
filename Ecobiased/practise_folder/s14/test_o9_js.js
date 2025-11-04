define('o9.NiFiInbound', ['o9/data/query', 'o9/data/cellset'], function () {
    Log.Info("Query opened");
    import fetch from "node-fetch";

    var ActionButtonCall = function (o9Params) {
        Log.Info("AB Triggered: inside ActionButtonCall");

        var parsedParams = JSON.parse(o9Params);
        var queryModule = require('o9/data/query');
        var cellsetModule = require('o9/data/cellset');

        // Date-time string
        var now = new Date();
        var pad = (n) => (n < 10 ? "0" + n : n);
        var IncomingCurrentDate =
            now.getFullYear() + "-" +
            pad(now.getMonth() + 1) + "-" +
            pad(now.getDate()) + ":" +
            pad(now.getHours()) + ":" +
            pad(now.getMinutes()) + ":" +
            pad(now.getSeconds());

        var resLocationNumber = parsedParams.locationNumber;
        var resPickupDate = parsedParams.pickupDate;
        var resId = parsedParams.id;

        // --- Input validations ---
        if (!resId) {
            RuleOutputToUI = { Status: 'Error', Message: 'Please enter Customer Order ID.' };
            return;
        }
        if (!resLocationNumber) {
            RuleOutputToUI = { Status: 'Error', Message: 'Please enter Location Number.' };
            return;
        }
        if (!resPickupDate) {
            RuleOutputToUI = { Status: 'Error', Message: 'Please enter Pickup Date.' };
            return;
        }
        if (!Array.isArray(parsedParams.items) || parsedParams.items.length === 0) {
            RuleOutputToUI = { Status: 'Error', Message: 'Please provide at least one item with itemNumber and quantity.' };
            return;
        }

		// Global-like variables (like in your NiFi Python)
		var Json_to_attribute = "";
		var id_to_db = "";
		var output_list = [];
		var output_length = 0;
		var output_quantity_list = [];
		var output_item_quantity = [];

		// 1. Json_to_attribute (stringified JSON)
		Json_to_attribute = JSON.stringify(parsedParams);

		// 2. id_to_db (quoted id)
		id_to_db = `'${resId}'`;

		// 3. Extract item numbers and quantities
		parsedParams.items.forEach(function (item) {
			output_list.push(item.itemNumber);
			output_quantity_list.push(item.quantity);
		});

		// 4. Build itemNumber_quantity list
		for (var i = 0; i < output_list.length; i++) {
			output_item_quantity.push(output_list[i] + "_" + output_quantity_list[i]);
		}

		// 5. Unique item numbers (array)
		function uniqueList(list) {
			var seen = {};
			var unique = [];
			list.forEach(function (val) {
				if (!seen[val]) {
					seen[val] = true;
					unique.push(val);
				}
			});
			return unique;
		}
		output_list = uniqueList(output_list);

		// 6. Length of unique items
		output_length = output_list.length;

		// 7. Format output_item_quantity as "(item_qty,item_qty,...)"
		output_item_quantity = "(" + output_item_quantity.join(",") + ")";

		Log.Info("Json_to_attribute: " + Json_to_attribute);
		Log.Info("id_to_db: " + id_to_db);
		Log.Info("output_list (array): " + JSON.stringify(output_list));
		Log.Info("output_length: " + output_length);
		Log.Info("output_quantity_list: " + JSON.stringify(output_quantity_list));
		Log.Info("output_item_quantity: " + output_item_quantity);

		var ConcatenateMultiselect = function(value) {
			if (Array.isArray(value)) {
				return '"' + value.join('","') + '"';
			}
			return value;
		};

	var output_list_str = ConcatenateMultiselect(output_list);
	Log.Info("output_list_str: " + output_list_str);

	//var output1 = `(select (&CWV * [SCSItem].[Item].filter(#.Name in {${output_list_str}}) * [SCSLocation].[Location].[${resLocationNumber}]) on row,({if (Measure.[Delivered_Frozen] == True) then if (Measure.[DeliveryDate_1] < "${resPickupDate}") then 1 else 0 else if (Measure.[DeliveryDate_1] <= "${resPickupDate}") then 1 else 0 as transient.[ValidDelivery]})on column).count;`;
	var output1 = `select (&CWV * [SCSItem].[Item].filter(#.Name in {${output_list_str}}) * [SCSLocation].[Location].[${resLocationNumber}]) on row,({if (Measure.[Delivered_Frozen] == True) then if (Measure.[DeliveryDate_1] < "${resPickupDate}") then 1 else 0 else if (Measure.[DeliveryDate_1] <= "${resPickupDate}") then 1 else 0 as transient.[ValidDelivery]})on column;`;
	Log.Info("Up to here1: ");
	var query = cellsetModule.createCellSet(queryModule.select(output1));
	Log.Info("Up to here2: ");
	var output1_1=query.rowCount;
	Log.Info("Up to here3: " + output1_1);
	Log.Info("output1_1: " );
	output_query = (output1_1 === output_length) ? output1 : null;
	Log.Info("final_output_query: " + output_query);

	const o9_PLATFORM_API_URL_FACT = "https://o9cprcert.starbucks.net/api/v2/fact/StarbucksCPR"; // Replace with your actual base URL
	const filters = [
      { AttributeName: "Item", Values: output_list },
      { AttributeName: "Location", Values: [resLocationNumber] }
    ];

    const url = `${o9_PLATFORM_API_URL_FACT}/ItemxStore1?Filters=${encodeURIComponent(JSON.stringify(filters))}&size=20`;
    Log.Info("url is  " + url);
    // Perform GET request
    async function callAPI() {
      try {
        const response = await fetch(url, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            "Authorization": "ApiKey mjbt1dbw.gifrys7pzkyi143lme9bbdz"
          }
        });

        if (!response.ok) {
          Log.Info("Response not okay");
          return;
        }

        const data = await response.json();
        Log.Info("API Response:", data);
      } catch (error) {
        Log.Info("API Request Failed:", error);
      }
    }
    callAPI();
        // --- Loop through items ---
        parsedParams.items.forEach(function (it, i) {
            if (!it.itemNumber || !it.quantity || isNaN(it.quantity) || it.quantity < 0) {
                RuleOutputToUI = {
                    Status: 'Error',
                    Message: `Invalid item at index ${i}: itemNumber and quantity are required, quantity must be >= 0`,
                };
                return;
            }

            var resItemNumber = it.itemNumber;
            var resQuantity = it.quantity;

            // Check if a record already exists for same combination
            var dupQuery = `
				Select(
                    Version.[Version Name].[CurrentWorkingView] *
                    [SCSItem].[Item].[${resItemNumber}] *
                    [SCSLocation].[Location].[${resLocationNumber}] *
                    [CustomerOrderID].[CustomerOrderID].[${resId}] *
                    [Time].[Day].[${resPickupDate}]
                ) on row, ({Measure.[COQtyJS]}) on column WHERE {Measure.[COQtyJS] == ${resQuantity}};
                `;
			Log.Info("duplicate validation query: " +JSON.stringify(dupQuery));

			var dupCellsetObj = cellsetModule.createCellSet(queryModule.select(dupQuery));

            var isDuplicate = false;
            if (dupCellsetObj.rowCount > 0) {
					isDuplicate = true;
            }

            // --- Decide COReasonCodeJS ---
            var reasonCode = isDuplicate ? 400 : 202;
            var statusMsg = isDuplicate ? 'Order already exist' : '';

            // --- Insert / Update query ---
            var insertQuery = `cartesian scope:(
                Version.[Version Name].[CurrentWorkingView] *
                [SCSItem].[Item].[${resItemNumber}] *
                [SCSLocation].[Location].[${resLocationNumber}] *
                [CustomerOrderID].[CustomerOrderID].[${resId}] *
                [Time].[Day].filter(#.Key == todatetime("${resPickupDate}"))
            );
            Measure.[COQtyJS] = ${resQuantity};
            Measure.[IncomingCurrentDate] = todatetime("2022-09-30");
            Measure.[COReasonCodeJS] = ${reasonCode};
            Measure.[COStatusJS] = "${statusMsg}";
            end scope;`;
			Log.Info("Insert query " + insertQuery);
            queryModule.update(insertQuery);

            Log.Info("Inserted itemNumber=" + resItemNumber +
                     ", quantity=" + resQuantity +
                     ", COReasonCodeJS=" + reasonCode +
                     (isDuplicate ? " (duplicate)" : " (new)"));
        });
    };

    return { ActionButtonCall: ActionButtonCall };
});