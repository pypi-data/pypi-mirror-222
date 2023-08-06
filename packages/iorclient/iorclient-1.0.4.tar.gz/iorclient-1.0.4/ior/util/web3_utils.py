import json

import web3.middleware
from web3 import Web3
from web3.contract import Contract
from web3.contract.contract import ContractFunctions, ContractEvents, ContractFunction


def get_web3(provider: str, is_print: bool = False, is_add_poa=False) -> Web3:
    """
    创建web3实例
    :param provider: web3提供者
    :param is_print: 是否打印状态
    :param is_add_poa: 是否增加poa
    :return:
    """
    w3 = Web3(Web3.HTTPProvider(provider))

    # https://web3py.readthedocs.io/en/latest/web3.contract.html#contract-functions
    # 关闭强类型限制
    w3.strict_bytes_type_checking = False
    # w3.middleware_onion.add(web3.middleware.geth_poa_middleware)
    # w3.middleware_onion.add(web3.middleware.pythonic_middleware)
    # w3.middleware_onion.add(web3.middleware.abi_middleware)
    if is_add_poa:
        w3.middleware_onion.add(web3.middleware.geth_poa_middleware)
    else:
        w3.middleware_onion.inject(web3.middleware.geth_poa_middleware, layer=0)
    if is_print:
        print(f"连接状态 => {w3.is_connected()}")
        print(f"最近一个块 => {w3.eth.get_block('latest')}")
        print(f"版本 => {w3.client_version}")
    return w3

def to_address(data):
    return Web3.to_checksum_address(data)

def to_hex(data):
    return Web3.to_hex(data)

def to_json(data):
    return Web3.to_json(data)

def to_text(data):
    return Web3.to_text(data)

def keccak256(data: str):
    return Web3.keccak(text=data)

def get_abi(filename: str):
    """
    从文件里获取abi
    :param filename:
    :return:
    """
    with open(filename, 'r', encoding='utf-8')as f:
        obj = json.load(f)
        if not obj:
            raise IOError(f"{filename}文件非法")
        if 'abi' not in obj:
            raise IOError(f"{filename}文件不包含abi")
        return obj['abi']

def get_abi_bytecode(filename: str):
    """
    从文件里获取abi
    :param filename:
    :return:
    """
    with open(filename, 'r', encoding='utf-8')as f:
        obj = json.load(f)
        if not obj:
            raise IOError(f"{filename}文件非法")
        if 'abi' not in obj:
            raise IOError(f"{filename}文件不包含abi")
        return obj['abi'],obj['bytecode']

def contract_instance(w3: Web3, address: str, abi) -> Contract:
    """
    获取合约
    :param w3:
    :param address:
    :param abi:
    :return:
    """
    return w3.eth.contract(address=address, abi=abi)


def contract_functions(instance: Contract) -> ContractFunctions:
    """
    获取合约所有函数
    :param instance:
    :return:
    """
    return instance.functions


def contract_events(instance: Contract) -> ContractEvents:
    """
    获取合约所有事件
    :param instance:
    :return:
    """
    return instance.events

def util_estimate_transaction(w3: Web3, public_key: str, func: ContractFunction):              
    tx = func.build_transaction({
        "gasPrice": 0, #w3.eth.gas_price,
        # 'gas': 50000,
        "from": public_key,
        "nonce": w3.eth.get_transaction_count(public_key)
    })
    print(tx)
    return tx

def util_sign_transaction(w3: Web3, tx, private_key: str):
    signed_txn = w3.eth.account.sign_transaction(tx, private_key=private_key)
    return signed_txn
    #signed_txn.rawTransaction

def util_send_raw_transaction(w3: Web3, rawTx, timeout: int, poll_latency: int):
    tx_hash = w3.eth.send_raw_transaction(rawTx)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=timeout, poll_latency=poll_latency)
    return receipt

def util_process_receipt(event, receipt, key, logIndex=0):
    logs = event.process_receipt(receipt)
    key = logs[logIndex]['args'][key]
    return receipt, key


def create_account(w3):
    """
    创建账户
    :param w3:
    :return:
    """
    acc = w3.eth.account.create()
    pk = acc.key.hex()
    pub = acc.address
    return pub,pk
