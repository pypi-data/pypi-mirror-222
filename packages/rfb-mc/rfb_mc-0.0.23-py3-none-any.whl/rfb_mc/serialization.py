from ast import literal_eval
from typing import Dict, Tuple, TypedDict, Any, Literal, Counter, Optional

from rfb_mc.restrictive_formula_module import get_restrictive_formula_module
from rfb_mc.store import StoreData
from rfb_mc.types import RfBmcTask, RfBmcResult, Params, BmcTask, BmcResult


def v1_encode_rf_bmc_task(task: RfBmcTask) -> str:
    return repr((
        task.rfm_guid,
        get_restrictive_formula_module(task.rfm_guid).encode_restrictive_formula_params(
            task.rfm_formula_params,
        ),
        task.a,
        task.q
    ))


def v1_decode_rf_bmc_task(task: str) -> RfBmcTask:
    rfm_guid, rfm_formula_params, a, q = literal_eval(task)

    return RfBmcTask(
        rfm_guid=rfm_guid,
        rfm_formula_params=get_restrictive_formula_module(rfm_guid).decode_restrictive_formula_params(
            rfm_formula_params,
        ),
        a=a,
        q=q
    )


def v1_encode_rf_bmc_result(result: RfBmcResult) -> str:
    return repr(tuple(result))


def v1_decode_rf_bmc_result(result: str) -> RfBmcResult:
    return RfBmcResult(*literal_eval(result))


def v1_encode_rf_bmc_task_result(task_result: Tuple[RfBmcTask, RfBmcResult]) -> str:
    return repr((
        v1_encode_rf_bmc_task(task_result[0]),
        v1_encode_rf_bmc_result(task_result[1])
    ))


def v1_decode_rf_bmc_task_result(task_result: str) -> Tuple[RfBmcTask, RfBmcResult]:
    task, result = literal_eval(task_result)

    return (
        v1_decode_rf_bmc_task(task),
        v1_decode_rf_bmc_result(result),
    )


def v1_encode_bmc_task(task: BmcTask) -> str:
    return repr((
        task.a,
    ))


def v1_decode_bmc_task(task: str) -> BmcTask:
    a, = literal_eval(task)

    return BmcTask(
        a=a,
    )


def v1_encode_bmc_result(result: BmcResult) -> str:
    return repr(tuple(result))


def v1_decode_bmc_result(result: str) -> BmcResult:
    return BmcResult(*literal_eval(result))


def v1_encode_bmc_task_result(task_result: Tuple[BmcTask, BmcResult]) -> str:
    return repr((
        v1_encode_bmc_task(task_result[0]),
        v1_encode_bmc_result(task_result[1])
    ))


def v1_decode_bmc_task_result(task_result: str) -> Tuple[BmcTask, BmcResult]:
    task, result = literal_eval(task_result)

    return (
        v1_decode_bmc_task(task),
        v1_decode_bmc_result(result),
    )


SerializedV1RfBmcResultsMap = Dict[str, int]


def v1_encode_rf_bmc_results_map(
    rf_bmc_results_map: Dict[RfBmcTask, Counter[RfBmcResult]],
) -> SerializedV1RfBmcResultsMap:
    return {
        v1_encode_rf_bmc_task_result((task, result)): rf_bmc_results_map[task][result]
        for task in rf_bmc_results_map
        for result in rf_bmc_results_map[task]
    }


def v1_decode_rf_bmc_results_map(
    rf_bmc_results_map: SerializedV1RfBmcResultsMap,
) -> Dict[RfBmcTask, Counter[RfBmcResult]]:
    task_results = list(map(v1_decode_rf_bmc_task_result, rf_bmc_results_map.keys()))

    tasks = set([task for task, _ in task_results])

    return {
        task: Counter[RfBmcResult]({
            result: int(rf_bmc_results_map[v1_encode_rf_bmc_task_result((task, result))])
            for result in [task_result[1] for task_result in task_results if task_result[0] == task]
        })
        for task in tasks
    }


class SerializedV1Params(TypedDict):
    bit_width_counter: Dict[str, int]


def v1_encode_params(params: Params) -> SerializedV1Params:
    return {
        "bit_width_counter": {
            str(key): params.bit_width_counter[key]
            for key in params.bit_width_counter.keys()
        }
    }


def v1_decode_params(params: SerializedV1Params) -> Params:
    return Params(
        bit_width_counter=Counter[int]({
            int(key): int(params["bit_width_counter"][key])
            for key in params["bit_width_counter"]
        })
    )


# Python representation of the store data with native types,
# i.e. processable using pickle, repr/literal_eval and json.
class SerializedV1StoreData(TypedDict):
    version: Literal[1]
    params: SerializedV1Params
    rf_bmc_results_map: SerializedV1RfBmcResultsMap
    bmc_task_result: Optional[str]


def v1_encode_store_data(data: StoreData) -> SerializedV1StoreData:
    return SerializedV1StoreData(
        version=1,
        params=v1_encode_params(data.params),
        rf_bmc_results_map=v1_encode_rf_bmc_results_map(
            data.rf_bmc_results_map,
        ),
        bmc_task_result=None if data.bmc_task_result is None else v1_encode_bmc_task_result(data.bmc_task_result),
    )


def v1_decode_store_data(data: SerializedV1StoreData) -> StoreData:
    return StoreData(
        params=v1_decode_params(data["params"]),
        rf_bmc_results_map=v1_decode_rf_bmc_results_map(data["rf_bmc_results_map"]),
        bmc_task_result=None if data["bmc_task_result"] is None else v1_decode_bmc_task_result(data["bmc_task_result"]),
    )


def decode_store_data(data: Any) -> Tuple[int, StoreData]:
    """
    Decodes a serialized store data item of any known version,
    returns the version it was encoded in and the interpreted store data
    """

    if data["version"] == 1:
        typed_item: SerializedV1StoreData = data
        return data["version"], v1_decode_store_data(typed_item)
    else:
        raise ValueError(f"Unexpected version \"{data['version']}\" in store data entry")
