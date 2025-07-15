# Changelog

## [2.2.0](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/tree/2.2.0) (2025-07-15)

[Full Changelog](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/compare/2.1.0...2.2.0)

**Implemented enhancements:**

- feat: Support nested defaults [\#154](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/154) ([maksym-iv](https://github.com/maksym-iv))
- fix: Support for "null" value in arguments\_specs defaults [\#151](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/151) ([maksym-iv](https://github.com/maksym-iv))

**Merged pull requests:**

- chore\(deps\): update dependency pytest to v8.4.1 [\#153](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/153) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency mypy to v1.16.1 [\#152](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/152) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency pytest-cov to v6.2.1 [\#150](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/150) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency pytest to v8.4.0 [\#149](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/149) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency mypy to v1.16.0 [\#148](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/148) ([renovate[bot]](https://github.com/apps/renovate))
- fix\(deps\): update dependency typer to ^0.16.0 [\#146](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/146) ([renovate[bot]](https://github.com/apps/renovate))
- fix\(deps\): update dependency typer to v0.15.4 [\#144](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/144) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency pylint to v3.3.7 [\#143](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/143) ([renovate[bot]](https://github.com/apps/renovate))
- fix\(deps\): update dependency typer to v0.15.3 [\#142](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/142) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update actions/setup-python digest to a26af69 [\#141](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/141) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency pytest-cov to v6.1.1 [\#140](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/140) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency pytest-cov to v6.1.0 [\#139](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/139) ([renovate[bot]](https://github.com/apps/renovate))

## [2.1.0](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/tree/2.1.0) (2025-03-27)

[Full Changelog](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/compare/2.0.1...2.1.0)

**Implemented enhancements:**

- \[Enhancement\] Add support for Ansible documentation markup [\#125](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/issues/125)
- add basic handling of Ansible doc markup [\#127](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/127) ([s3lph](https://github.com/s3lph))

**Fixed bugs:**

- \[Bug\] Readme template markdown.j2 breaks table rendering due to missing whitespace. [\#123](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/issues/123)
- \[Bug\] aar-doc defaults produces invalid YAML when duming sequence-of-mapping [\#120](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/issues/120)
- \[Bug\] Ansible can't parse generated defaults due to unquoted colons [\#119](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/issues/119)
- quote strings containing colons [\#122](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/122) ([s3lph](https://github.com/s3lph))
- proper indentation of sequence-of-mapping [\#121](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/121) ([s3lph](https://github.com/s3lph))

**Merged pull requests:**

- Update linting and tests  [\#138](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/138) ([rndmh3ro](https://github.com/rndmh3ro))
- chore\(deps\): update actions/setup-python digest to 8d9ed9a [\#137](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/137) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency pylint to v3.3.6 [\#135](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/135) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency pre-commit to v4.2.0 [\#134](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/134) ([renovate[bot]](https://github.com/apps/renovate))
- Extend Codeowners [\#133](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/133) ([schurzi](https://github.com/schurzi))
- chore\(deps\): update dependency python to 3.13 [\#131](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/131) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency pylint to v3.3.5 [\#130](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/130) ([renovate[bot]](https://github.com/apps/renovate))
- fix\(deps\): update dependency jinja2 to v3.1.6 \[security\] [\#129](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/129) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency pytest to v8.3.5 [\#128](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/128) ([renovate[bot]](https://github.com/apps/renovate))
- fix\(deps\): update dependency typer to v0.15.2 [\#126](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/126) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): pin dependencies [\#118](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/118) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency mypy to v1.15.0 [\#117](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/117) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency pylint to v3.3.4 [\#116](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/116) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update actions/setup-python digest to 4237552 [\#115](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/115) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency isort to v6 [\#114](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/114) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency black to v25 [\#113](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/113) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency pre-commit to v4.1.0 [\#112](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/112) ([renovate[bot]](https://github.com/apps/renovate))
- fix\(deps\): update dependency ruamel-yaml to v0.18.10 [\#111](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/111) ([renovate[bot]](https://github.com/apps/renovate))
- fix\(deps\): update dependency ruamel-yaml to v0.18.8 [\#110](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/110) ([renovate[bot]](https://github.com/apps/renovate))
- fix\(deps\): update dependency ruamel-yaml to v0.18.7 [\#109](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/109) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency mypy to v1.14.1 [\#108](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/108) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency pylint to v3.3.3 [\#107](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/107) ([renovate[bot]](https://github.com/apps/renovate))
- fix\(deps\): update dependency jinja2 to v3.1.5 [\#106](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/106) ([renovate[bot]](https://github.com/apps/renovate))
- fix\(deps\): update dependency click to v8.1.8 [\#105](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/105) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency mypy to v1.14.0 [\#104](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/104) ([renovate[bot]](https://github.com/apps/renovate))
- fix\(deps\): update dependency typer to v0.15.1 [\#103](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/103) ([renovate[bot]](https://github.com/apps/renovate))
- fix\(deps\): update dependency typer to ^0.15.0 [\#102](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/102) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency pylint to v3.3.2 [\#101](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/101) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency pytest to v8.3.4 [\#100](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/100) ([renovate[bot]](https://github.com/apps/renovate))
- fix\(deps\): update dependency typer to ^0.14.0 [\#99](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/99) ([renovate[bot]](https://github.com/apps/renovate))
- fix\(deps\): update dependency typer to v0.13.1 [\#98](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/98) ([renovate[bot]](https://github.com/apps/renovate))
- fix\(deps\): update dependency typer to ^0.13.0 [\#97](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/97) ([renovate[bot]](https://github.com/apps/renovate))

## [2.0.1](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/tree/2.0.1) (2024-11-01)

[Full Changelog](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/compare/2.0.0...2.0.1)

**Fixed bugs:**

- \[Bug\] URL to role metadata in README.md broken [\#93](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/issues/93)

**Merged pull requests:**

- chore\(deps\): update dependency pytest-cov to v6 [\#96](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/96) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update actions/setup-python digest to 0b93645 [\#95](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/95) ([renovate[bot]](https://github.com/apps/renovate))
- doc: Fix Ansible Galaxy role metadata URL [\#94](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/94) ([lingling9000](https://github.com/lingling9000))
- chore\(deps\): update actions/checkout action to v4.2.2 [\#92](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/92) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update actions/checkout digest to 11bd719 [\#91](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/91) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency mypy to v1.13.0 [\#90](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/90) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency mypy to v1.12.1 [\#89](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/89) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency mypy to v1.12.0 [\#88](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/88) ([renovate[bot]](https://github.com/apps/renovate))

## [2.0.0](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/tree/2.0.0) (2024-10-14)

[Full Changelog](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/compare/1.2.0...2.0.0)

**Implemented enhancements:**

- \[Enhancement\] The markdown template should include the content of the description field [\#78](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/issues/78)
- Feature/generate defaults [\#81](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/81) ([moritzrp](https://github.com/moritzrp))
- feat\(template\): add description to markdown template [\#79](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/79) ([rndmh3ro](https://github.com/rndmh3ro))

**Fixed bugs:**

- \[Bug\] aar-doc command unknown after installation [\#75](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/issues/75)

**Closed issues:**

- \[Bug\] output\_template not used [\#69](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/issues/69)

**Merged pull requests:**

- chore\(deps\): update dependency black to v24.10.0 [\#86](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/86) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency pre-commit to v4.0.1 [\#85](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/85) ([renovate[bot]](https://github.com/apps/renovate))
- Fix/stuff [\#84](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/84) ([rndmh3ro](https://github.com/rndmh3ro))
- chore\(deps\): update actions/checkout action to v4.2.1 [\#83](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/83) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update actions/checkout digest to eef6144 [\#82](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/82) ([renovate[bot]](https://github.com/apps/renovate))
- chore\(deps\): update dependency pre-commit to v4 [\#80](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/80) ([renovate[bot]](https://github.com/apps/renovate))
- Change entry point to aar-doc  [\#76](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/76) ([moritzrp](https://github.com/moritzrp))

## [1.2.0](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/tree/1.2.0) (2024-09-30)

[Full Changelog](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/compare/1.1.0...1.2.0)

**Implemented enhancements:**

- fix\(aar\_doc\): handle tilde home-expansion [\#74](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/74) ([rndmh3ro](https://github.com/rndmh3ro))

## [1.1.0](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/tree/1.1.0) (2024-09-29)

[Full Changelog](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/compare/1.0.4...1.1.0)

**Implemented enhancements:**

- \[Enhancement\] Pypi publish latest releases [\#58](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/issues/58)
- Feature/examples in docs [\#71](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/71) ([rndmh3ro](https://github.com/rndmh3ro))
- feat\(meta\): add support for reading from meta/main [\#68](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/68) ([rndmh3ro](https://github.com/rndmh3ro))

**Fixed bugs:**

- \[Bug\] aar\_doc does not support arguments\_spec in meta/main.yaml [\#66](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/issues/66)

**Merged pull requests:**

- Linting [\#73](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/73) ([rndmh3ro](https://github.com/rndmh3ro))
- feat\(docs\): update readme [\#72](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/72) ([rndmh3ro](https://github.com/rndmh3ro))
- chore\(deps\): update actions/checkout action to v4.2.0 [\#70](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/70) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency pytest to v8.3.3 [\#67](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/67) ([renovate[bot]](https://github.com/apps/renovate))
- Update actions/setup-python digest to f677139 [\#65](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/65) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency typer to v0.12.5 [\#64](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/64) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency mypy to v1.11.2 [\#63](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/63) ([renovate[bot]](https://github.com/apps/renovate))

## [1.0.4](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/tree/1.0.4) (2024-08-22)

[Full Changelog](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/compare/1.0.3...1.0.4)

**Fixed bugs:**

- Create version-drafter.yml [\#61](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/61) ([rndmh3ro](https://github.com/rndmh3ro))
- update whole release-workflow [\#60](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/60) ([rndmh3ro](https://github.com/rndmh3ro))
- change if-condition to match name of repo [\#59](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/59) ([rndmh3ro](https://github.com/rndmh3ro))

**Merged pull requests:**

- add gh app branch protection token [\#62](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/62) ([rndmh3ro](https://github.com/rndmh3ro))
- Update dependency typer to v0.12.4 [\#57](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/57) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency PyYAML to v6.0.2 [\#56](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/56) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency black to v24.8.0 [\#55](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/55) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency mypy to v1.11.1 [\#54](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/54) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency pytest to v8.3.2 [\#53](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/53) ([renovate[bot]](https://github.com/apps/renovate))
- Update patrickjahns/version-drafter-action digest to 2076fa4 [\#52](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/52) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency pytest to v8.3.1 [\#51](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/51) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency mypy to v1.11.0 [\#50](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/50) ([renovate[bot]](https://github.com/apps/renovate))
- Update actions/setup-python digest to 39cd149 [\#49](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/49) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency mypy to v1.10.1 [\#48](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/48) ([renovate[bot]](https://github.com/apps/renovate))
- Update actions/checkout digest to 692973e [\#47](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/47) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency pytest to v8.2.2 [\#46](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/46) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency mypy to v1.10.0 [\#45](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/45) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency black to v24.4.2 [\#44](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/44) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency Jinja2 to v3.1.4 [\#43](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/43) ([renovate[bot]](https://github.com/apps/renovate))
- Update actions/checkout digest to a5ac7e5 [\#42](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/42) ([renovate[bot]](https://github.com/apps/renovate))
- Update actions/checkout digest to 1d96c77 [\#41](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/41) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency black to v24.4.0 [\#40](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/40) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency typer to v0.12.3 [\#39](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/39) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency typer to v0.12.1 [\#38](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/38) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency typer to ^0.12.0 [\#37](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/37) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency typer to ^0.11.0 [\#36](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/36) ([renovate[bot]](https://github.com/apps/renovate))
- Update actions/setup-python digest to 82c7e63 [\#35](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/35) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency pytest-cov to v5 [\#34](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/34) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency typer to ^0.10.0 [\#33](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/33) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency pytest to v8.1.1 [\#32](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/32) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency black to v24.3.0 [\#31](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/31) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency mypy to v1.9.0 [\#30](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/30) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency black to v24.2.0 [\#29](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/29) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency black to v24.1.1 [\#28](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/28) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency pytest to v8 [\#27](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/27) ([renovate[bot]](https://github.com/apps/renovate))
- Update juliangruber/read-file-action digest to b549046 [\#26](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/26) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency black to v24 [\#25](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/25) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency Jinja2 to v3.1.3 [\#24](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/24) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency mypy to v1.8.0 [\#23](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/23) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency pytest to v7.4.4 [\#22](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/22) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency black to v23.12.1 [\#21](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/21) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency isort to v5.13.2 [\#20](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/20) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency black to v23.12.0 [\#19](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/19) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency isort to v5.13.1 [\#18](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/18) ([renovate[bot]](https://github.com/apps/renovate))
- Update actions/setup-python action to v5 [\#17](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/17) ([renovate[bot]](https://github.com/apps/renovate))
- Pin dependencies [\#16](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/16) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency black to v23.11.0 [\#15](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/15) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency mypy to v1 [\#12](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/12) ([renovate[bot]](https://github.com/apps/renovate))

## [1.0.3](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/tree/1.0.3) (2023-11-03)

[Full Changelog](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/compare/1.0.2...1.0.3)

## [1.0.2](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/tree/1.0.2) (2023-11-02)

[Full Changelog](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/compare/1.0.1...1.0.2)

**Merged pull requests:**

- Update dependency pytest to v7.4.3 [\#14](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/14) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency black to v23.10.1 [\#13](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/13) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency black to v23 [\#11](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/11) ([renovate[bot]](https://github.com/apps/renovate))
- Update actions/checkout action to v4 [\#10](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/10) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency typer to ^0.9.0 [\#9](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/9) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency pytest-cov to v4.1.0 [\#8](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/8) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency pytest to v7.4.2 [\#7](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/7) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency isort to v5.12.0 [\#6](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/6) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency black to v22.12.0 [\#5](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/5) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency click to v8.1.7 [\#3](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/3) ([renovate[bot]](https://github.com/apps/renovate))
- Update dependency PyYAML to v6.0.1 [\#2](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/2) ([renovate[bot]](https://github.com/apps/renovate))
- Configure Renovate [\#1](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/pull/1) ([renovate[bot]](https://github.com/apps/renovate))

## [1.0.1](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/tree/1.0.1) (2023-08-08)

[Full Changelog](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/compare/1.0.0...1.0.1)

## [1.0.0](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/tree/1.0.0) (2023-08-08)

[Full Changelog](https://github.com/telekom-mms/Automated-Ansible-Role-Documentation/compare/c419c32eb35222ffe48c80e869c34d3676a675a5...1.0.0)



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
