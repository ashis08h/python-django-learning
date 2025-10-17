import json
import sys
import traceback
from java.nio.charset import StandardCharsets
from org.apache.commons.io import IOUtils
from org.apache.nifi.processor.io import StreamCallback
from org.python.core.util import StringUtil

Json_to_attribute = ''
id_to_db = ''
output_list = []
output_length = ''
output_query = ''
output_quantity_list = []
output_item_quantity = []


class TransformCallback(StreamCallback):
    def init(self):
        pass

    def process(self, inputStream, outputStream):
        try:
            # Read input FlowFile content
            input_text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
            input_json = json.loads(input_text)
            input_json = input_json

            global Json_to_attribute
            Json_to_attribute = str(input_json)
            Json_to_attribute = Json_to_attribute.replace("u'", '"')
            Json_to_attribute = Json_to_attribute.replace("':", '":')
            Json_to_attribute = Json_to_attribute.replace(",'", ',"')
            Json_to_attribute = Json_to_attribute.replace("',", '",')

            items_list = input_json["items"]

            global output_list
            global output_length
            global output_quantity_list
            global output_item_quantity

            for key in items_list:
                output_list.append(key['itemNumber'])
                output_quantity_list.append(key['quantity'])

            for i in range(len(output_list)):
                output_item_quantity.append(str(output_list[i]) + "_" + str(output_quantity_list[i]))

            # Get the unique item listfor hive query
            def unique_list(list1):
                unique_list = []
                for x in list1:
                    if x not in unique_list:
                        unique_list.append(x)
                return (unique_list)

            output_list = unique_list(output_list)
            output_length = len(output_list)
            output_list = str(output_list)
            output_list = output_list.replace("[", "")
            output_list = output_list.replace("]", "")

            output_item_quantity = str(output_item_quantity)
            output_item_quantity = output_item_quantity.replace("[", "(")
            output_item_quantity = output_item_quantity.replace("]", ")")

            global output_query
            output_query = "Select count(*) payload_check FROM sbux.bod_lane_item_dim_after_range where store_number = " + str(
                input_json[
                    'locationNumber']) + " and item_number in " + output_list + " and (CASE WHEN delivered_frozen like 'true%' then delivery_date < '" + str(
                input_json['pickupDate']) + "' else delivery_date <= '" + str(
                input_json['pickupDate']) + "' END) having count(distinct(item_number)) = " + str(output_length)

            global id_to_db
            id_to_db = "'" + str(input_json["id"]) + "'"

            # Transform content
            transformed_json = input_json
            # Write output content
            output_text = json.dumps(transformed_json, indent=4)
            outputStream.write(StringUtil.toBytes(output_text))
        except:
            log.error('Error during transformation')
            log.error(traceback.format_exc())
            raise


flowFile = session.get()
if (flowFile != None):

    try:
        # All processing code starts at this indent
        log.debug("IN CUSTOM SCRIPT - Processing incoming file")
        flowFile = session.write(flowFile, TransformCallback())
        attrMap = {'list': output_list}
        flowFile = session.putAllAttributes(flowFile, attrMap)
        session.transfer(flowFile, REL_SUCCESS)
    except Exception as e:
        log.error('Error while processing flowfile')
        log.error(traceback.format_exc())
        session.transfer(flowFile, REL_FAILURE)