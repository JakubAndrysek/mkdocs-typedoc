# Mkdocs-Typedoc Plugin

The Mkdocs-Typedoc Plugin is designed to integrate TypeDoc documentation with your MkDocs project.

## Installation

Install the plugin using pip from [PyPI](https://pypi.org/project/mkdocs-typedoc/):

```bash
pip install mkdocs-typedoc
```

Ensure that you have [Node.js](https://nodejs.org/en/) installed in your system. If not, you can download it from the official website.

Also, install [TypeDoc](https://typedoc.org/) using [NPM](https://www.npmjs.com/):

```bash
npm install typedoc --save-dev
```

## Usage

Add the following lines to your mkdocs.yml:

```yaml
plugins:
  - typedoc:
      source: './ts-examples/@types/*.d.ts'
      output_dir: 'typedocApi'
      tsconfig: './ts-examples/tsconfig.json'
      options: 'typedoc.json'
      name: 'API Doc'
```

- `source` (required): The path to your TypeScript source code.
- `output_dir` (optional): The directory where you want to output your docs. Default is "typedoc".
- `tsconfig` (required): The path to the tsconfig file for your project.
- `options` (optional): The path to the typedoc.json options file with more options.
- `name` (optional): The name for the generated documentation. Default is "TypeDoc API".

The plugin will generate TypeDoc documentation into the output directory specified.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Do You Enjoy My Work?
Then definitely consider:

- supporting me on GitHub Sponsors: [![](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86)](https://github.com/sponsors/jakubandrysek)

## License

[MIT](https://choosealicense.com/licenses/mit/)