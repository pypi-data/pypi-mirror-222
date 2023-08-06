import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';
import {
  ICommandPalette,
  Dialog,
  InputDialog,
  showErrorMessage
} from '@jupyterlab/apputils';
import { CodeCell } from '@jupyterlab/cells';
import { NotebookPanel, INotebookTracker } from '@jupyterlab/notebook';
import { beautifyPythonCode } from './beautifierscript';
import { IMainMenu } from '@jupyterlab/mainmenu';
import { Menu } from '@lumino/widgets';
import { createRepoFile } from './linksharing';
import { KernelMessage } from '@jupyterlab/services';

function presentDialog(message: string) {
  const dialog = new Dialog({
    title: message,
    buttons: [
      Dialog.okButton({ label: 'OK', displayType: 'default', accept: true })
    ]
  });
  dialog.launch();
}

const plugin: JupyterFrontEndPlugin<void> = {
  id: 'Dropdown menu extension:plugin',
  description:
    'A JupyterLab dropdown extension for additional jupyterlab features!',
  autoStart: true,
  requires: [ICommandPalette, INotebookTracker, IMainMenu],
  activate: (
    app: JupyterFrontEnd,
    palette: ICommandPalette,
    notebookTracker: INotebookTracker,
    mainMenu: IMainMenu
  ) => {
    const { commands } = app;
    const beautifyCommand = 'beautify:python-code';
    commands.addCommand(beautifyCommand, {
      label: 'Beautify Python Code',
      execute: () => {
        const current: NotebookPanel | null = notebookTracker.currentWidget;
        if (current === null) {
          return;
        }
        const cell: CodeCell | null = current.content.activeCell as CodeCell;
        if (cell === null) {
          return;
        }
        let codeBefore = cell.model.toJSON().source;
        if (Array.isArray(codeBefore)) {
          codeBefore = codeBefore.join('\n');
        }
        const codeAfter = beautifyPythonCode(codeBefore);
        presentDialog('Selected Code Beautified');
        app.commands.execute('notebook:replace-selection', { text: codeAfter });
      }
    });

    palette.addItem({
      command: beautifyCommand,
      category: 'Extension Commands'
    });

    const anomalyCommand = 'anomaly-detection:get-csv';
    commands.addCommand(anomalyCommand, {
      label: 'Get Anomalies from CSV',
      execute: () => {
        fetch('http://localhost:5000/anomaly', {
          method: 'POST'
        })
          .then(response => response.text())
          .then(data => presentDialog(data))
          .catch(error => {
            console.error('Error:', error);
          });
      }
    });
    palette.addItem({
      command: anomalyCommand,
      category: 'Extension Commands'
    });

    const regenCommand = 'regen-dataframe:get-csv';
    commands.addCommand(regenCommand, {
      label: 'Regenerate DataFrame from CSV',
      execute: () => {
        fetch('http://localhost:5000/regen', {
          method: 'POST'
        })
          .then(response => response.text())
          .then(data => presentDialog(data))
          .catch(error => {
            console.error('Error:', error);
          });
      }
    });
    palette.addItem({
      command: regenCommand,
      category: 'Extension Commands'
    });
    const columnCommand = 'column-correlator:get-csv';
    commands.addCommand(columnCommand, {
      label: 'Correlate columns from CSV',
      execute: () => {
        fetch('http://localhost:5000/correlator', {
          method: 'POST'
        })
          .then(response => response.text())
          .then(data => presentDialog(data))
          .catch(error => {
            console.error('Error:', error);
          });
      }
    });
    palette.addItem({
      command: columnCommand,
      category: 'Extension Commands'
    });
    const missingCommand = 'missing-filler:get-csv';
    commands.addCommand(missingCommand, {
      label: 'Fill NaN values from CSV',
      execute: () => {
        fetch('http://localhost:5000/missing', {
          method: 'POST'
        })
          .then(response => response.text())
          .then(data => presentDialog(data))
          .catch(error => {
            console.error('Error:', error);
          });
      }
    });
    palette.addItem({
      command: missingCommand,
      category: 'Extension Commands'
    });

    const sharingCommand = 'jp-option-4:main-menu';
    commands.addCommand(sharingCommand, {
      label: 'Sharing',
      execute: async (args: any) => {
        const { shareChoice } = args;

        const current: NotebookPanel | null = notebookTracker.currentWidget;
        if (current === null) {
          alert('There is no active notebook.');
          return;
        }
        const cell: CodeCell | null = current.content.activeCell as CodeCell;
        if (cell === null) {
          alert('There is no active cell in the notebook.');
          return;
        }

        let codeBefore = cell.model.toJSON().source;
        if (Array.isArray(codeBefore)) {
          codeBefore = codeBefore.join('\n');
        }

        if (!codeBefore) {
          alert('The active cell is empty. There is no code to share.');
          return;
        }
        const sessionContext = current.sessionContext;
        const future = sessionContext.session?.kernel?.requestExecute({
          code: codeBefore
        });
        let codeOutput = '';
        if (future) {
          future.onIOPub = msg => {
            if (msg.header.msg_type === 'execute_result') {
              const executeResultMsg = msg as KernelMessage.IExecuteResultMsg;
              codeOutput += executeResultMsg.content.data['text/plain'] + '\n';
            } else if (msg.header.msg_type === 'display_data') {
              const displayDataMsg = msg as KernelMessage.IDisplayDataMsg;
              codeOutput += displayDataMsg.content.data['text/plain'] + '\n';
            } else if (msg.header.msg_type === 'stream') {
              const streamMsg = msg as KernelMessage.IStreamMsg;
              codeOutput += streamMsg.content.text + '\n';
            }
          };
          await future.done;
        }
        let repoFileContent = '';
        if (shareChoice === '1') {
          repoFileContent = codeBefore.toString();
        } else if (shareChoice === '2') {
          repoFileContent = codeOutput;
        } else if (shareChoice === '3') {
          repoFileContent = `# Code:\n\n${codeBefore}\n\n# Output:\n\n${codeOutput}`;
        } else {
          alert('Invalid choice. Please enter 1, 2 or 3.');
          return;
        }

        let tokenDialog = await InputDialog.getText({
          title: 'Enter your GitHub token:'
        });

        while (tokenDialog.value === null || tokenDialog.value === '') {
          if (tokenDialog.button.accept) {
            await showErrorMessage(
              'Input Error',
              'GitHub token must not be empty.'
            );
            tokenDialog = await InputDialog.getText({
              title: 'Enter your GitHub token:'
            });
          } else {
            return;
          }
        }
        const token = tokenDialog.value;

        let ownerDialog = await InputDialog.getText({
          title: 'Enter the GitHub repository owner:'
        });

        while (ownerDialog.value === null || ownerDialog.value === '') {
          if (ownerDialog.button.accept) {
            await showErrorMessage(
              'Input Error',
              'GitHub repository owner must not be empty.'
            );
            ownerDialog = await InputDialog.getText({
              title: 'Enter the GitHub repository owner:'
            });
          } else {
            return;
          }
        }
        const owner = ownerDialog.value;

        let repoDialog = await InputDialog.getText({
          title: 'Enter the GitHub repository name:'
        });

        while (repoDialog.value === null || repoDialog.value === '') {
          if (repoDialog.button.accept) {
            await showErrorMessage(
              'Input Error',
              'GitHub repository name must not be empty.'
            );
            repoDialog = await InputDialog.getText({
              title: 'Enter the GitHub repository name:'
            });
          } else {
            return;
          }
        }
        const repo = repoDialog.value;

        let pathDialog = await InputDialog.getText({
          title:
            'Enter the path where you want to create the file in the repository:'
        });

        while (pathDialog.value === null || pathDialog.value === '') {
          if (pathDialog.button.accept) {
            await showErrorMessage(
              'Input Error',
              'Repository file path must not be empty.'
            );
            pathDialog = await InputDialog.getText({
              title:
                'Enter the path where you want to create the file in the repository:'
            });
          } else {
            return;
          }
        }
        const path = pathDialog.value;

        let messageDialog = await InputDialog.getText({
          title: 'Enter a commit message:'
        });

        while (messageDialog.value === null || messageDialog.value === '') {
          if (messageDialog.button.accept) {
            await showErrorMessage(
              'Input Error',
              'Commit message must not be empty.'
            );
            messageDialog = await InputDialog.getText({
              title: 'Enter a commit message:'
            });
          } else {
            return;
          }
        }
        const message = messageDialog.value;

        const repoFileUrl = await createRepoFile(
          token,
          owner,
          repo,
          path,
          repoFileContent,
          message
        );
        if (repoFileUrl) {
          presentDialog(`Your sharable link is: ${repoFileUrl}`);
        } else {
          presentDialog(
            'Failed to create a repo file. Please check your inputs and try again.'
          );
        }
      }
    });

    // Create sub-menu options
    const shareCodeCommand = 'share:code';
    commands.addCommand(shareCodeCommand, {
      label: 'Share Code',
      execute: () => commands.execute(sharingCommand, { shareChoice: '1' })
    });

    palette.addItem({
      command: shareCodeCommand,
      category: 'Extension Commands'
    });

    const shareOutputCommand = 'share:output';
    commands.addCommand(shareOutputCommand, {
      label: 'Share Output',
      execute: () => commands.execute(sharingCommand, { shareChoice: '2' })
    });

    palette.addItem({
      command: shareOutputCommand,
      category: 'Extension Commands'
    });

    const shareBothCommand = 'share:both';
    commands.addCommand(shareBothCommand, {
      label: 'Share Both',
      execute: () => commands.execute(sharingCommand, { shareChoice: '3' })
    });

    palette.addItem({
      command: shareBothCommand,
      category: 'Extension Commands'
    });

    const sharingSubMenu = new Menu({ commands });
    sharingSubMenu.title.label = 'Sharing';
    sharingSubMenu.addItem({ command: shareCodeCommand });
    sharingSubMenu.addItem({ command: shareOutputCommand });
    sharingSubMenu.addItem({ command: shareBothCommand });

    const myMenu = new Menu({ commands });
    myMenu.title.label = 'Additional Features';
    myMenu.addItem({ command: beautifyCommand });
    myMenu.addItem({ command: anomalyCommand });
    myMenu.addItem({ command: regenCommand });
    myMenu.addItem({ command: columnCommand });
    myMenu.addItem({ command: missingCommand });
    myMenu.addItem({ type: 'submenu', submenu: sharingSubMenu });
    mainMenu.addMenu(myMenu, true, { rank: 1000 });
  }
};

export default plugin;
