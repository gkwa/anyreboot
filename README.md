# anyreboot

## Motivation

I love pyscaffold.

No, i mean I really love it.

...but it generates a lot of scaffold and lately I discovered `rye` and I like how it uses the pyproject.toml--something I've wondered how to use.

I like how how few files I need to install a script.

## Summary

Taking rye for a spin

```bash
docker run --rm -ti python bash -c 'pip install git+https://github.com/taylormonacelli/anyreboot && find /usr/local/lib/python3.12/site-packages/anyreboot -name mymain.tmpl && hello'
```
