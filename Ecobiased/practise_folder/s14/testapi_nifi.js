define('o9.NiFiInbound', ['o9/data/query', 'o9/data/cellset'], function () {
    Log.Info("Query opened");

    var ActionButtonCall = function (o9Params) {
        Log.Info("AB Triggered: inside ActionButtonCall");

        var parsedParams = JSON.parse(o9Params);

        // Good: serialize before logging
        Log.Info("ParsedParams.id: " + parsedParams.id);
        Log.Info("ParsedParams.items (json): " + JSON.stringify(parsedParams.items));
        Log.Info("ParsedParams.locationNumber (json): " + JSON.stringify(parsedParams.locationNumber));
        Log.Info("ParsedParams.pickupDate (json): " + JSON.stringify(parsedParams.pickupDate));

        var resLocationNumber = parsedParams.locationNumber;
        var resPickupDate = parsedParams.pickupDate;
        var resId = parsedParams.id;

        if (parsedParams.id == null) {
			Log.Info("Raising error for no inputs");
			RuleOutputToUI = {
				Status: 'Error',
				Message: 'Please enter Customer Order ID.'
			};
			// Exit if validation failed
			return;
		}

		if (parsedParams.locationNumber == null) {
			Log.Info("Raising error for no inputs");
			RuleOutputToUI = {
				Status: 'Error',
				Message: 'Please enter Location Number.'
			};
			// Exit if validation failed
			return;
		}

		if (parsedParams.pickupDate == null) {
			Log.Info("Raising error for no inputs");
			RuleOutputToUI = {
				Status: 'Error',
				Message: 'Please enter Pickup Date.'
			};
			// Exit if validation failed
			return;
		}

		// Validate items
        if (!Array.isArray(parsedParams.items) || parsedParams.items.length === 0) {
            RuleOutputToUI = { Status: 'Error', Message: 'Please provide at least one item with itemNumber and quantity.' };
            return;
        }

        // Or log each item on its own line
        if (Array.isArray(parsedParams.items)) {
            parsedParams.items.forEach(function (it, i) {
                if (!it.itemNumber || !it.quantity || isNaN(it.quantity) || it.quantity < 0) {
                    RuleOutputToUI = {
                        Status: 'Error',
                        Message: `Invalid item at index ${i}: itemNumber and quantity are required, quantity must be >= 0.`
                    };
                    return; // stop processing further
                }
                Log.Info("items[" + i + "] itemNumber=" + it.itemNumber + ", quantity=" + it.quantity);
                var resItemNumber = it.itemNumber;
                var resQuantity = it.quantity;
                query = `cartesian scope:(Version.[Version Name].[CurrentWorkingView] * [SCSItem].[Item].[${resItemNumber}] * [SCSLocation].[Location].[${resLocationNumber}] * [CustomerOrderID].[CustomerOrderID].[${resId}] * [Time].[Day].[${resPickupDate}]);
                Measure.[COQtyJS] = ${resQuantity};
                end scope;`;
                queryModule.update(query);
                Log.Info("Created entry successfully of items[" + i + "] itemNumber=" + it.itemNumber + ", quantity=" + it.quantity);

            });
        }

        var queryModule = require('o9/data/query');
        var cellsetModule = require('o9/data/cellset');
    };

    return { ActionButtonCall: ActionButtonCall };
});


