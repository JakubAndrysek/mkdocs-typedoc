# Mkdocs-Typedoc Plugin

<p align="center">
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FJakubAndrysek%2Fmkdocs-typedoc&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=true"/></a>
<a href="https://github.com/JakubAndrysek/mkdocs-typedoc/blob/main/LICENSE" target="_blank"><img src="https://img.shields.io/github/license/JakubAndrysek/mkdocs-typedoc?style=flat-square"></a>
<a href="https://pypi.org/project/mkdocs-typedoc/" target="_blank"><img alt="PyPI" src="https://img.shields.io/pypi/v/mkdocs-typedoc?style=flat-square"></a>
<a href="https://github.com/JakubAndrysek/mkdocs-typedoc/stargazers" target="_blank"><img src="https://img.shields.io/github/stars/JakubAndrysek/mkdocs-typedoc?style=flat-square"></a>
<a href="https://github.com/JakubAndrysek/mkdocs-typedoc/forks" target="_blank"><img src="https://img.shields.io/github/forks/JakubAndrysek/mkdocs-typedoc?style=flat-square"></a>
<a href="https://github.com/JakubAndrysek/mkdocs-typedoc/issues" target="_blank"><img src="https://img.shields.io/github/issues/JakubAndrysek/mkdocs-typedoc?style=flat-square"></a>
<a href="https://github.com/JakubAndrysek/mkdocs-typedoc/discussions" target="_blank"><img src="https://img.shields.io/github/discussions/JakubAndrysek/mkdocs-typedoc?style=flat-square"></a>
<a href="https://pypistats.org/packages/mkdocs-typedoc" target="_blank"><img src="https://static.pepy.tech/personalized-badge/mkdocs-typedoc?period=month&units=international_system&left_color=black&right_color=orange&left_text=Downloads"></a>
</p>

The Mkdocs-Typedoc Plugin is designed to integrate TypeDoc documentation with your MkDocs project.

## Installation

Install the plugin using pip from [PyPI](https://pypi.org/project/mkdocs-typedoc/):

```bash
pip install mkdocs-typedoc
```

Ensure that you have [Node.js](https://nodejs.org/en/) installed in your system. If not, you can download it from the official website.

Also, install [TypeDoc](https://typedoc.org/) using [NPM](https://www.npmjs.com/):

```bash
npm install typedoc typescript --save-dev
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
      disable_system_check: False
```

- `source` (required): The path to your TypeScript source code.
- `output_dir` (optional): The directory where you want to output your docs. Default is "typedoc".
- `tsconfig` (required): The path to the tsconfig file for your project.
- `options` (optional): The path to the typedoc.json options file with more options.
- `name` (optional): The name for the generated documentation. Default is "TypeDoc API".
- `disable_system_check` (optional): Disable the TypeScript system check. Default is False.

The plugin will generate TypeDoc documentation into the output directory specified.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Do You Enjoy My Work?
Then definitely consider:

- supporting me on GitHub Sponsors: [![](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86)](https://github.com/sponsors/jakubandrysek)

## License

[MIT](https://choosealicense.com/licenses/mit/)