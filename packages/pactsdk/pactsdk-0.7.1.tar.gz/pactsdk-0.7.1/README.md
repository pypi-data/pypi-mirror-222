# Pact Python SDK

**pactsdk** is a software development kit for interfacing to [Pact](https://pact.fi), a decentralized automated market maker on the Algorand protocol.

The full documentation for this module can be found here:

[https://pactfi.github.io/pact-py-sdk/latest/](https://pactfi.github.io/pact-py-sdk/latest/)

The Python SDK provides a set of modules on top of the Algorand Python SDK for interacting with liquidity pools and making swaps.
Clients can use the Python SDK to enhance their trading experience with Pact.

What is covered by the library:

- Creating pools
- Managing liquidity
- Making swaps
- Farming

Signing and sending transactions is not covered by the library. The provided examples use algosdk directly to send the transactions.

# Installation

`pip install pactsdk`

# Basic usage

**CAUTION** - The library uses integers for asset amounts e.g. microalgos instead of algos so if you want to send 1 algo, you need to specify it as 1_000_000.

Create a Pact client.

```py
from algosdk.v2client.algod import AlgodClient
import pactsdk

algod = AlgodClient(token, url)
pact = pactsdk.PactClient(algod)
```

By default, the client is configured to work with mainnet. You can easily change it by providing `network` argument. The `network` argument changes the default values in `pact.config` object. It contains things like API URL or global contract ids.

```py
pact = pactsdk.PactClient(algod, network="testnet")
```

Fetching pools by assets pair. It uses Pact API to retrieve the pool. Can return multiple pools with differing fee_bps.

```py
algo = pact.fetch_asset(0)
other_coin = pact.fetch_asset(8949213)

pools = pact.fetch_pools_by_assets(algo, other_coin) # The pool will be fetched regardless of assets order.
```

You can fetch a pool by providing assets ids instead of Asset objects.

```py
pools = pact.fetch_pools_by_assets(0, 8949213)
```

You can also fetch a pool by providing app id. This way the pool is retrieved directly from the chain.

```py
pool = pact.fetch_pool_by_id(456321)
```

Before making the transactions you need to opt-in for the assets. There's no need to opt-in for algo.

```py
import algosdk

private_key = algosdk.mnemonic.to_private_key('<mnemonic>')
address = algosdk.account.address_from_private_key(private_key)

def opt_in(asset):
    is_opted_in = asset.is_opted_in(address)
    if not is_opted_in:
        opt_in_tx = asset.prepare_opt_in_tx(address)
        signed_tx = opt_in_tx.sign(private_key)
        algod.send_transaction(signed_tx)

opt_in(pool.primary_asset)
opt_in(pool.secondary_asset)
opt_in(pool.liquidity_asset) # Needed if you want to manage the liquidity.
```

Check the current pool state.

```py
print(pool.state)
# PoolState(
#   total_liquidity=900000,
#   total_primary=956659,
#   total_secondary=849972,
#   primary_asset_price=0.8884795940873393,
#   secondary_asset_price=1.1255182523659604,
# )
```

Explicit pool state update is necessary periodically and after each pool operation.

```py
pool.update_state()
pool.state  # Now holds fresh values.
```

Managing the liquidity.

```py
# Add liquidity.
liquidity_addition = pool.prepare_add_liquidity(
  primary_asset_amount=100_000,
  secondary_asset_amount=50_000,
);
add_liq_tx_group = liquidity_addition.prepare_tx_group(address)
signed_add_liq_tx_group = add_liq_tx_group.sign(private_key)
algod.send_transactions(signed_add_liq_tx_group)

# Remove liquidity.
remove_liq_tx_group = pool.prepare_remove_liquidity_tx_group(
  address=address,
  amount=100_000,
)
signed_remove_liq_tx_group = remove_liq_tx_group.sign(private_key)
algod.send_transactions(signed_remove_liq_tx_group)
```

Making a swap.

```py
swap = pool.prepare_swap(
  asset=algo,
  amount=200_000,
  slippage_pct=2,
)

# You can inspect swap effect before submitting the transaction.
print(swap.effect)
# SwapEffect(
#     amount_deposited=200000,
#     amount_received=146529,
#     minimum_amount_received=143598,
#     fee=441,
#     price=0.73485,
#     primary_asset_price_after_swap=0.6081680080300244,
#     secondary_asset_price_after_swap=1.6442824791774173,
#     primary_asset_price_change_pct=-31.549580645715963,
#     secondary_asset_price_change_pct=46.091142966447585,
# )

# Let's submit the swap.
swap_tx_group = swap.prepare_tx_group(address)
signed_tx_group = swap_tx_group.sign(private_key)
algod.send_transactions(signed_tx_group)
```

## Composability of transactions.

The SDK has two sets of methods for creating transactions:

1. `prepare_..._tx_group` e.g. `pool.prepare_swap_tx_group`

   Those methods are convenience methods which ask algod for suggested transaction parameters, build transactions and create a transaction group. You can't add you own transactions to the group using those methods.

2. `build_..._txs` e.g. `pool.build_swap_txs`

   Those methods return a list of transactions. You can extend that list with your own transactions and create a `TransactionGroup` manually from this list.

# Development

- `poetry install`

Development requires [Pact contracts V1](https://github.com/pactfi/algorand-testbed) to be checked out.

- `git clone git@github.com:pactfi/algorand-testbed.git`
- `cd algorand-testbed`
- `poetry install`
- `docker compose up -d`
- `cd ..`

## Building

- `poetry build`

You can install the package locally with
`pip install dist/pactsdk-<version>.whl`

Validate the installation `python -c "import pactsdk; print(pactsdk.__version__)"`

## Running tests

- `poetry run pytest`
