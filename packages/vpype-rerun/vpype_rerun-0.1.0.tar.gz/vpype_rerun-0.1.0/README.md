# vpype-rerun

This plug-in integrates the [Rerun viewer](https://github.com/rerun-io/rerun) in [*vpype*](https://github.com/abey79/vpype).

## Example

```
vpype random -n 500 -a 20cm 20cm rerun
```

<img width="1106" alt="image" src="https://github.com/abey79/vpype-rerun/assets/49431240/4bcadf27-3058-4c16-aaab-5ba5fe3e9252">


## Why?

This plug-in makes it easy to log large quantities of [2D line strips](https://www.rerun.io/docs/reference/data_types/linestrip2d) to the Rerun viewer, which is useful for stress-testing, etc.


## Installation

See the [installation instructions](https://vpype.readthedocs.io/en/latest/install.html) for information on how
to install `vpype` (TL;DR: `pipx install "vpype[all]"`).

If *vpype* was installed using pipx, use the following command:

```bash
$ pipx inject vpype vpype-rerun
```

If *vpype* was installed using pip in a virtual environment, activate the virtual environment and use the following command:

```bash
$ pip install vpype-rerun
```

## Documentation

The complete plug-in documentation is available directly in the CLI help:

```bash
$ vpype rerun --help
```


## License

See the [LICENSE](LICENSE) file for details.
