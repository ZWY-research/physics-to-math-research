# Optional Python Setup / 按需配置 Python 环境

These commands are instructions for users who choose to prepare an environment. This project does not automatically execute them, install or upgrade packages, or modify your existing environment. Choose only the packages needed for the task. This is documentation, not a runtime requirement.

以下命令供选择配置环境的用户手动执行。项目不会自动执行、安装或升级软件，也不会修改既有环境。只安装任务需要的库，本说明不是运行时要求。

## Check Python / 检查 Python

Windows PowerShell:

```powershell
py --version
# If the launcher is unavailable, check python instead.
python --version
```

Linux/macOS (bash/zsh):

```bash
python3 --version
```

Use an available Python 3 interpreter supported by your chosen package releases. If none is available, consult the [official Python downloads](https://www.python.org/downloads/) and your platform's instructions. Do not infer availability from these examples.

使用实际可用且满足所选库版本要求的 Python 3。若未安装，查看 [Python 官方下载](https://www.python.org/downloads/)及平台说明。这些示例不代表你的环境已经配置完成。

## Create a separate environment / 创建独立环境

Run in your chosen project directory. `.venv` should be a new environment path, not an existing environment you want to preserve. The [official venv documentation](https://docs.python.org/3/library/venv.html) documents both activation and direct interpreter use.

在自行选择的项目目录执行，`.venv` 应是新环境路径，不要覆盖需要保留的环境。[venv 官方文档](https://docs.python.org/3/library/venv.html)说明了激活及直接使用解释器两种方式。

Windows PowerShell (if `py` is unavailable, replace `py` with the available `python` for creation):

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
```

If PowerShell blocks activation, no execution-policy change is needed for the commands below: call the environment interpreter directly as `.\.venv\Scripts\python.exe` in place of `python`.

如果 PowerShell 阻止激活，不必为下列操作修改执行策略，直接用 `.\.venv\Scripts\python.exe` 替代 `python` 即可。

Linux/macOS (bash/zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
python --version
```

Without activation, use `.venv/bin/python` in place of `python`. If creation reports that venv/ensurepip is unavailable, follow your Python distributor's instructions before proceeding; this guide does not change system packages automatically.

无需激活时，用 `.venv/bin/python` 替代 `python`。若创建时提示缺少 venv／ensurepip，先按所用 Python 发行方说明处理；本指南不自动修改系统软件包。

## Install only what is needed / 按任务安装

After activation (or using the explicit environment interpreter), choose a relevant command rather than running all three:

激活后（或使用独立环境解释器），按任务选择命令，不必执行全部三项：

```text
python -m pip install sympy
python -m pip install scipy
python -m pip install pint
```

Commands follow [SymPy's installation guide](https://docs.sympy.org/latest/install.html), [SciPy's pip/venv guide](https://scipy.org/install/) and [Pint's installation section](https://pint.readthedocs.io/en/stable/getting/index.html#installation). `python -m pip` binds installation to the selected interpreter. No automatic upgrade or domain-specific software dependency is prescribed.

命令已按 [SymPy 官方安装说明](https://docs.sympy.org/latest/install.html)、[SciPy 的 pip／venv 说明](https://scipy.org/install/)和 [Pint 安装章节](https://pint.readthedocs.io/en/stable/getting/index.html#installation)核对。`python -m pip` 将安装绑定到选定解释器。不规定自动升级或领域专用软件依赖。

## Check imports / 检查导入

Run only checks for packages you installed:

仅检查已安装的库：

```text
python -c "import sympy; print(sympy.__version__)"
python -c "import scipy; print(scipy.__version__)"
python -c "import pint; print(pint.__version__)"
```

These check importability and versions, not mathematical correctness or scientific validation.

上述检查只确认可导入及版本，不证明数学正确性或科学有效性。

## Record the environment / 记录复现环境

```text
python -c "import sys; print(sys.version); print(sys.executable)"
python -m pip show sympy
python -m pip show scipy
python -m pip show pint
python -m pip freeze > requirements-used.txt
```

Use `pip show` only for installed packages; the record should reflect what was actually used. Save Python and relevant library versions, OS, scripts, input data permitted to be shared, assumptions and solver tolerances with the result. `pip freeze` is a snapshot of installed distributions, not a guarantee of cross-platform reproducibility; inspect local paths and private package locations before sharing it. The recorded file can later guide a deliberately chosen environment with `python -m pip install -r requirements-used.txt`.

只对已安装的库使用 `pip show`，记录应反映实际使用情况。随结果保存 Python 与相关库版本、操作系统、脚本、获准共享的输入、前提和求解器容限。`pip freeze` 是已安装发行包快照，不保证跨平台复现；共享前检查本地路径及私人包地址。以后自行选择复现环境时，可参考记录执行 `python -m pip install -r requirements-used.txt`。

After activation, `deactivate` returns the shell to the previous environment. No installation was executed as part of this documentation update. Numerical sampling is not a strict proof; see [tool selection and limits](index.md).

激活环境后，执行 `deactivate` 可退出。本轮文档更新未执行任何安装。数值抽样不是严格证明，参见[工具选择与限制](index.md)。
