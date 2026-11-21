# oa.oa_types

Types for oa

### Functions

| `heatmap_of_models_and_their_fields`()   |    |
|------------------------------------------|----|

### Classes

| [`BatchRequest`](#oa.oa_types.BatchRequest)(\*, custom_id, method, url, body)     |                                                                                |
|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [`BatchRequestBody`](#oa.oa_types.BatchRequestBody)(\*, input, model)                 |                                                                                |
| [`EmbeddingResponse`](#oa.oa_types.EmbeddingResponse)(\*, id, custom_id, ...)          |                                                                                |
| [`InputDataJsonL`](#oa.oa_types.InputDataJsonL)                                     |                                                                                |
| [`InputText`](#oa.oa_types.InputText)(\*, input)                               | Used to specify the input data in some OpenAI API endpounts.                   |
| [`JsonL`](#id0)([root])                                      | A generic class for JSONL (JSON Lines) files, which are lists of dictionaries. |
| `JsonL[InputText]`([root])                                                                          | A generic class for JSONL (JSON Lines) files, which are lists of dictionaries. |
| [`RequestResponse`](#oa.oa_types.RequestResponse)(\*, status_code, request_id, body) |                                                                                |
| [`Response`](#id2)(\*, id, custom_id, response, error)       |                                                                                |
| [`ResponseBody`](#oa.oa_types.ResponseBody)(\*, object, data, model, usage)       |                                                                                |
| [`Response[Embedding]`](#oa.oa_types.EmbeddingResponse)(\*, id, custom_id, ...)        |                                                                                |
| `RootModel[list[TypeVar]]`([root])                                                                  | !!! abstract "Usage Documentation"                                             |
| [`Usage`](#oa.oa_types.Usage)(\*, prompt_tokens, total_tokens)             |                                                                                |

### *class* oa.oa_types.BatchRequest(, custom_id, method, url, body)

Bases: `BaseModel`

#### model_config *: [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

### *class* oa.oa_types.BatchRequestBody(, input, model)

Bases: `BaseModel`

#### model_config *: [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

### *class* oa.oa_types.EmbeddingResponse(, id, custom_id, response, error)

Bases: [`Response`](#id2)

#### model_config *: [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

### oa.oa_types.InputDataJsonL

alias of `JsonL[InputText]`

### *class* oa.oa_types.InputText(, input)

Bases: `BaseModel`

Used to specify the input data in some OpenAI API endpounts.

#### model_config *: [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

### *class* oa.oa_types.JsonL(root=PydanticUndefined)

Bases: `RootModel[list[TypeVar]]`, [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic)[`T`]

A generic class for JSONL (JSON Lines) files, which are lists of dictionaries.

#### model_config *: [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

### *class* oa.oa_types.JsonL(root=PydanticUndefined)

Bases: `RootModel[list[TypeVar]]`, [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic)[`T`]

A generic class for JSONL (JSON Lines) files, which are lists of dictionaries.

#### model_config *: [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

### *class* oa.oa_types.RequestResponse(, status_code, request_id, body)

Bases: `BaseModel`, [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic)[`DatumT`]

#### model_config *: [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

### *class* oa.oa_types.Response(, id, custom_id, response, error)

Bases: `BaseModel`, [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic)[`DatumT`]

#### model_config *: [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

### *class* oa.oa_types.Response(, id, custom_id, response, error)

Bases: `BaseModel`, [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic)[`DatumT`]

#### model_config *: [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

### *class* oa.oa_types.ResponseBody(, object, data, model, usage)

Bases: `BaseModel`, [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic)[`DatumT`]

#### model_config *: [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

### *class* oa.oa_types.Usage(, prompt_tokens, total_tokens)

Bases: `BaseModel`

#### model_config *: [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar)[ConfigDict]* *= {}*

Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].
