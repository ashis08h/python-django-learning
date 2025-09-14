define('o9.NGP.InboundSync', ['o9/data/query', 'o9/data/cellset'], function () {
    var queryModule = require('o9/data/query');
	var cellsetModule = require('o9/data/cellset');

    function ValidateSupplier(SupplierID) {
        var querySupplierCheck = `(Select ([Supplier].[Supplier Location].filter(#.Name in {[${SupplierID}]}))).count;`;
        Log.Info("Log- querySupplierCheck: " + querySupplierCheck);

        var response = queryModule.update(querySupplierCheck);
        Log.Info("Log- querySupplierCheckResponse: " + response);

        return JSON.parse(response).Result == 1
            ? { Status: "Success", Status_Message: "" }
            : { Status: "Failure", Status_Message: `${SupplierID} is not present in Supplier Master` };
    }

    function ValidatePO_POLine(POHeaderID, POLineID) {
        var query = `(select (Version.[Version Name].[CurrentWorkingView] * [Purchase Orders].[PO ID].[${POHeaderID}] * [Document Line].[Line ID].[${POLineID}]) on row).count;`;
        Log.Info("Log- queryPO_POLineCheck: " + query);

        var response = queryModule.update(query);
        Log.Info("Log- queryPO_POLineCheckResponse: " + response);

        return JSON.parse(response).Result == 1
            ? { Status: "Success", Status_Message: "" }
            : { Status: "Failure", Status_Message: `${POHeaderID} and ${POLineID} is not a valid PO-PO Line combination` };
    }

    function ValidateMaterial(MaterialNumber) {
        var query = `(Select ([Item].[Item].filter(#.Name in {[${MaterialNumber}]}))).count;`;
        Log.Info("Log- queryMaterialCheck: " + query);

        var response = queryModule.update(query);
        Log.Info("Log- queryMaterialCheckResponse: " + response);

        return JSON.parse(response).Result == 1
            ? { Status: "Success", Status_Message: "" }
            : { Status: "Failure", Status_Message: `${MaterialNumber} is not present in Material Master` };
    }

	function ValidateLocation(Plant) {
        var query = `(Select ([Location].[Location].filter(#.Name in {[${Plant}]}))).count;`;
        Log.Info("Log- queryLocationCheck: " + query);

        var response = queryModule.update(query);
        Log.Info("Log- queryLocationCheckResponse: " + response);

        return JSON.parse(response).Result == 1
            ? { Status: "Success", Status_Message: "" }
            : { Status: "Failure", Status_Message: `${Plant} is not present in Location Master` };
    }

    var PO = function (o9Params) {
        Log.Info("Log-Started JavaScript o9.InboundSync.PO");
        var ParsedParams = JSON.parse(o9Params);
        Log.Info('Log- Fields...' + JSON.stringify(ParsedParams));

        let { POHeaderID, SupplierID, POCreationDate, Currency, PODocumentDate, POType, IncoTermCode } = ParsedParams.header;
        let Status_Message = [];

        let supplierValidation = ValidateSupplier(SupplierID);
        if (supplierValidation.Status === "Failure") return supplierValidation;

        for (let detail of ParsedParams.details) {
            let materialValidation = ValidateMaterial(detail.MaterialNumber);
            if (materialValidation.Status === "Failure") {
                Status_Message.push(materialValidation.Status_Message);
            }
			let locationValidation = ValidateLocation(detail.Plant);
            if (locationValidation.Status === "Failure") {
                Status_Message.push(locationValidation.Status_Message);
            }
        }

        if (Status_Message.length > 0) {
            return { Status: "Failure", Status_Message: Status_Message.join("; ") };
        }

           // START:- Create PO and PO Line if there are no errors
            var queryCreatePO = `CREATEMEMBER([Purchase Orders].[PO ID] = {, "${POHeaderID}"});`;
            Log.Info("Log- queryCreatePO : " + queryCreatePO);

            var queryCreatePOResponse = queryModule.update(queryCreatePO);
            Log.Info("Log- queryCreatePOResponse : " + queryCreatePOResponse);
            Status_Message = POHeaderID + ` created successfully`;

			var queryupdateIncoterm = `updatemember([Purchase Orders].[PO ID]={,"${POHeaderID}"}, [Purchase Orders].[Incoterm1]={"${IncoTermCode}",});`;
			Log.Info("Log- queryupdateIncoterm : " + queryupdateIncoterm);

			var queryupdateIncotermResponse = queryModule.update(queryupdateIncoterm);
			Log.Info("Log- queryupdateIncotermResponse : " + queryupdateIncotermResponse);

            // Loop through details and extract each field into separate variables and create PO Details
            ParsedParams.details.forEach((detail, index) => {
                let POLineId = detail.POLineId;
                let Plant = detail.Plant;
                let StorageLocation = detail.StorageLocation;
                let MaterialNumber = detail.MaterialNumber;
                let PoLineQty = detail.PoLineQty.trim();
                let NetPrice = detail.NetPrice.trim();
                let UnitPrice = detail.UnitPrice.trim();
                let DelvryDate = detail.DelvryDate;
                let ShipmentDate = detail.ShipmentDate;
                let OrderingUOM = detail.OrderingUOM;
                let ItemCategory = detail.ItemCategory;
                let ConfContKey = detail.ConfContKey;
                let OrderPriceUnit = detail.OrderPriceUnit;
				let PODelSchLineID = detail.PODelSchLineID;
				let POSchQty = detail.POSchQty;
				let pdtInDays = (new Date(DelvryDate) - new Date(ShipmentDate)) / 86400000;
				Log.Info("Log-****** pdtInDays: " + pdtInDays);

				let queryCreatePODetails = `cartesian scope: (Version.[Version Name].[CurrentWorkingView] * [Location].[Location].[${Plant}] * [Supplier].[Supplier Location].[${SupplierID}] * [PO Type].[PO Type].[${POType}] * [Purchase Orders].[PO ID].[${POHeaderID}] * [Item].[Item].[${MaterialNumber}] * [Document Line].[Line ID].[${POLineId}]);
					Measure.[ERP PO Line Requested Quantity]=${PoLineQty};
					Measure.[ERP PO Line Requested Amount]=${NetPrice};
					Measure.[ERP PO Line Storage Location]=${StorageLocation};
					Measure.[ERP PO Line Requested Ship Date]="${ShipmentDate}";
					Measure.[ERP PO Line Unit Price]=${UnitPrice};
					Measure.[ERP PO Line Proposed Unit Price]=${UnitPrice};
					Measure.[ERP PO Line Ordering UOM]="${OrderingUOM}";
					Measure.[ERP PO Line Item Category]="${ItemCategory}";
					Measure.[ERP PO Line Unit Price Multiplier]=${OrderPriceUnit};
					Measure.[ERP PO Line Order Multiple]=1;
					Measure.[ERP PO Line Request Modified Time]= now();
					Measure.[ERP PO Line Confirmation Control Key]="${ConfContKey}";
					Measure.[ERP PO Line Grouping]=37;
					Measure.[ERP PO Line Grouping for Invoice]=37;
					Measure.[ERP PO Line PDT in Days]=${pdtInDays};
					end scope;`;

                Log.Info("Log-** queryCreatePODetails : " + queryCreatePODetails);
                var queryCreatePODetailsResponse = queryModule.update(queryCreatePODetails);
                Log.Info("Log-******** *****queryCreatePOResponse : " + queryCreatePODetailsResponse);

				let queryCreatePODetailsHeader = `cartesian scope: (Version.[Version Name].[CurrentWorkingView] * [Location].[Location].[${Plant}] * [Supplier].[Supplier Location].[${SupplierID}] * [PO Type].[PO Type].[${POType}] * [Purchase Orders].[PO ID].[${POHeaderID}] * [Item].[Item].[${MaterialNumber}]);
					Measure.[ERP PO Header Creation Date] = "${POCreationDate}";
					Measure.[ERP PO Header Unit Price Currency]	=${Currency};
					Measure.[ERP PO Header E Invoice Indicator]	= "YES";
					Measure.[ERP PO Header Latest Revision]	=0;
					Measure.[ERP PO Header Document Date] ="${PODocumentDate}";
					Measure.[ERP PO Header Modified On] = now();
					end scope;`;

				Log.Info("Log-** queryCreatePODetailsHeader : " + queryCreatePODetailsHeader);
                var queryCreatePODetailsHeaderResponse = queryModule.update(queryCreatePODetailsHeader);
                Log.Info("Log-******** *****queryCreatePOHeaderResponse : " + queryCreatePODetailsHeaderResponse);

				let queryCreatePODetailsDS = `cartesian scope: (Version.[Version Name].[CurrentWorkingView] * [Location].[Location].[${Plant}] * [Supplier].[Supplier Location].[${SupplierID}] * [PO Type].[PO Type].[${POType}] * [Purchase Orders].[PO ID].[${POHeaderID}] * [Item].[Item].[${MaterialNumber}] * [Document Line].[Line ID].[${POLineId}] * [Document Schedule].[Delivery Schedule].[${PODelSchLineID}]);
					Measure.[ERP PO Schedule Requested Quantity] =${POSchQty};
					Measure.[ERP PO Schedule Requested Ship Date] ="${ShipmentDate}";
					Measure.[ERP PO Schedule Requested Delivery Date]="${DelvryDate}";
					Measure.[ERP PO Schedule Received Quantity] =0;
					end scope;`;

				Log.Info("Log-** queryCreatePODetailsDS : " + queryCreatePODetailsDS);
                var queryCreatePODetailsDSResponse = queryModule.update(queryCreatePODetailsDS);
                Log.Info("Log-******** *****queryCreatePODSResponse : " + queryCreatePODetailsDSResponse);


				let queryCreatePODetailsConfAssoc = `cartesian scope: (Version.[Version Name].[CurrentWorkingView] * [Location].[Location].[${Plant}] * [Supplier].[Supplier Location].[${SupplierID}] * [PO Type].[PO Type].[${POType}] * [Purchase Orders].[PO ID].[${POHeaderID}] * [Item].[Item].[${MaterialNumber}] * [Document Line].[Line ID].[${POLineId}] * [Confirmation Schedule].[Confirmation Schedule].[1]);
					Measure.[NGP PO Line Confirmation Association] = 1;
					end scope;`;

				Log.Info("Log-** queryCreatePODetailsConfAssoc : " + queryCreatePODetailsConfAssoc);
                var queryCreatePODetailsConfAssocResponse = queryModule.update(queryCreatePODetailsConfAssoc);
                Log.Info("Log-******** *****queryCreatePOConfAssocResponse : " + queryCreatePODetailsConfAssocResponse);

			});  // END:- Create PO and PO Line


        return { Status: "Success", Status_Message: `${POHeaderID} created successfully` };
    };

var Conf = function (o9Params) {
        Log.Info("Log-Started JavaScript o9.InboundSync.Conf");
        var ParsedParams = JSON.parse(o9Params);
        Log.Info('Log- Fields for Conf...' + JSON.stringify(ParsedParams));


        let Status_Message = [];
        let statusArray = [];

			// Loop through POConfirmation and extract each field into separate variables
			ParsedParams.POConfirmation.forEach((confirmation, index) => {
				let POHeaderID = confirmation.POHeaderID;
				let POLineID = confirmation.POLineID;
				let POConfSchID = confirmation.POConfSchID;
				let POConfQty = confirmation.POConfQty;
				let POConfDate = confirmation.POConfDate;
				let POCommitRef = confirmation.POCommitRef;


            let validationPO_POLine = ValidatePO_POLine(confirmation.POHeaderID, confirmation.POLineID);
            if (validationPO_POLine.Status === "Failure") {
                statusArray.push("Failure");
                Status_Message.push(validationPO_POLine.Status_Message);
            } else {
			var poContextQuery = 'select ( Version.[Version Name].[CurrentWorkingView] * [Purchase Orders].[PO ID].['+POHeaderID+'] * [Document Line].[Line ID].['+POLineID+'] * [Supplier].[Supplier Location] * [Location].[Location] * [PO Type].[PO Type] * [Item].[Item]) on row, ({Measure.[NGP Final PO Line Requested Quantity]}) on column;';

			Log.Info("Log-****** POContext Query for POHeader ID: "+POHeaderID+" and POLine ID: "+POLineID+" ... " + poContextQuery);

			var poContextData = queryModule.select(poContextQuery);
			poContextData = cellsetModule.createCellSet(poContextData);

			var Location = "", Item = "", SupplierLocation = "", POType = "";

			if (poContextData !== null && poContextData !== undefined && poContextData.rowCount !== 0) {
				Location = (poContextData.row(0).cell(poContextData.memberColumnIndex('Location', 'Location')).Name);
				Item = (poContextData.row(0).cell(poContextData.memberColumnIndex('Item', 'Item')).Name);
				SupplierLocation = (poContextData.row(0).cell(poContextData.memberColumnIndex('Supplier', 'Supplier Location')).Name);
				POType = (poContextData.row(0).cell(poContextData.memberColumnIndex('PO Type', 'PO Type')).Name);
			}

			 Log.Info("Log-****** SupplierLocation: " + SupplierLocation);
			 Log.Info("Log-****** Location: " + Location);
			 Log.Info("Log-****** POType: " + POType);
			 Log.Info("Log-****** Item: " + Item);

			// Get IncoTerm and Leadtime using IBPL query
			var query = 'Select ([Version].[Version Name].[CurrentWorkingView] * [Location].[Location].['+Location+'] * [Item].[Item].['+Item+'] *  [Purchase Orders].[PO ID].['+POHeaderID+'] * [Supplier].[Supplier Location].['+SupplierLocation+'] * [PO Type].[PO Type].['+POType+'] * [Document Line].[Line ID].['+POLineID+'] ) on row, ({Measure.[NGP PO Line Incoterm Type], Measure.[NGP Final PO Line Requested Ship Date], Measure.[NGP Final PO Line Requested Delivery Date], datediff(Measure.[NGP Final PO Line Requested Ship Date], Measure.[NGP Final PO Line Requested Delivery Date], Day) as Transient.Leadtime}) on column;';

			Log.Info("Running query for POHeaderID: "+POHeaderID+", POLineID: "+POLineID+" ... " + query);
			var queryData = queryModule.select(query);
			queryData = cellsetModule.createCellSet(queryData);

			var IncoTerm = "", LeadTimeMS = 0;
			if (queryData !== null && queryData !== undefined && queryData.rowCount !== 0) {
				IncoTerm = queryData.row(0).cell(queryData.measureColumnIndex('NGP PO Line Incoterm Type'));
				LeadTimeMS = queryData.row(0).cell(queryData.measureColumnIndex('Leadtime'));
			}

			Log.Info("IncoTerm: " + IncoTerm);
			Log.Info("Leadtime: " + LeadTimeMS);

			// Compute POConfShipDate and POConfDelDate
			let confDate = new Date(POConfDate);
			var POConfShipDate = "", POConfDelDate = "";

			if (IncoTerm === 'Prepaid') {
				POConfDelDate = formatDate(new Date(confDate));
				POConfShipDate = formatDate(new Date(confDate.getTime() - (LeadTimeMS * 24 * 60 * 60 * 1000)));
			} else {
				POConfDelDate = formatDate(new Date(confDate.getTime() + (LeadTimeMS * 24 * 60 * 60 * 1000)));
				POConfShipDate = formatDate(new Date(confDate));
			}

			Log.Info("POConfShipDate: " + POConfShipDate);
			Log.Info("POConfDelDate: " + POConfDelDate);

			// Utility function to format date
			function formatDate(date) {
				return date.getFullYear() + '-' +
					   (date.getMonth() + 1).toString().padStart(2, '0') + '-' +
					   date.getDate().toString().padStart(2, '0');
			}


			var queryUpdateInboundConfirm = `cartesian scope:(Version.[Version Name].[CurrentWorkingView] * [Location].[Location].[${Location}] * [Supplier].[Supplier Location].[${SupplierLocation}] * [PO Type].[PO Type].[${POType}] * [Purchase Orders].[PO ID].[${POHeaderID}] * [Document Line].[Line ID].[${POLineID}] * [Item].[Item].[${Item}] * [Confirmation Schedule].[Confirmation Schedule].[${POConfSchID}]);
			Measure.[NGP PO Confirmation Commit Reference Number] = coalesce(Measure.[NGP Final PO Confirmation Commit Reference Number],${POCommitRef});
			Measure.[ERP PO Confirmations Delivery Date] = "${POConfDelDate}";
			Measure.[ERP PO Confirmations Quantity] = ${POConfQty};
			Measure.[ERP PO Confirmations Ship Date] = "${POConfShipDate}";
			Measure.[NGP PO Line Confirmation Association] = 1;
			Measure.[ERP PO Confirmations Modified On] = now();
			Measure.[ERP PO Confirmations Changed By] = "ERP";
			Measure.[ERP PO Confirmations Modified By]= "Buyer";
			end scope;`;

			Log.Info("Log-************************queryUpdateInboundConfirm : "+queryUpdateInboundConfirm);
			var queryUpdateConfirmResponse = queryModule.update(queryUpdateInboundConfirm);
			Log.Info("Log-************************queryUpdateConfirmResponse : "+queryUpdateConfirmResponse);


			};

                Status_Message.push(`Confirmation created successfully for PO: ${confirmation.POHeaderID} - POLine: ${confirmation.POLineID}`);
                statusArray.push("Success");
        });

        let finalStatus = statusArray.includes("Failure")
            ? (statusArray.includes("Success") ? "Partial Success" : "Failure")
            : "Success";

        return { Status: finalStatus, Status_Message: Status_Message.join("; ") };
    };

    return {
        PO: PO,
        Conf: Conf
    };
});