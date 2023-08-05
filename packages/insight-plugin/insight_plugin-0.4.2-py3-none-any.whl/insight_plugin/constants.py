BOLD = "\033[1m"
UNDERLINE = "\033[4m"
ITALICS = "\033[3m"
END = "\033[0m"

CREATE_DESCRIPTION = (
    BOLD
    + "Create a new plugin."
    + END
    + ITALICS
    + " This command will generate the skeleton folder structure and "
    "code for a new plugin, based on the provided plugin.spec.yaml file"
    + END
)
SERVER_DESCRIPTION = (
    BOLD
    + "Run the plugin in HTTP mode."
    + END
    + ITALICS
    + " This allows an external API testing program to be "
    "used to test a plugin "
    + END
)
SAMPLES_DESCRIPTION = (
    BOLD
    + "Create test samples for actions and triggers."
    + END
    + ITALICS
    + " This command will create new files under the 'tests' folder "
    "which can be used to test each new action/trigger. "
    "Note if a file already exists for a particular action/trigger, it will not be overwritten."
    + END
)
REFRESH_DESCRIPTION = (
    BOLD
    + "Refresh the plugin."
    + END
    + ITALICS
    + " This command will update the current plugin code, when updates  are made in the "
    "plugin.spec.yaml file"
    + END
)
RUN_DESCRIPTION = (
    BOLD
    + "Run an action/trigger from a json test file"
    + END
    + ITALICS
    + " (created during sample generation)"
    + END
)
SHELL_DESCRIPTION = (
    BOLD
    + "Run the plugin via the docker shell"
    + END
    + ITALICS
    + " to enable advanced debugging"
    + END
)
EXPORT_DESCRIPTION = (
    BOLD
    + "Export a plugin Docker image to a tarball."
    + END
    + ITALICS
    + " This tarball can be uploaded as a custom plugin via the import "
    "functionality in the InsightConnect UI"
    + END
)
VALIDATE_DESCRIPTION = (
    BOLD
    + "Validate / Run checks against the plugin."
    + END
    + ITALICS
    + " This command performs quality control checks on the current "
    "state of the plugin. This should be run before finalizing any new updates."
    + END
)
VERSION_DESCRIPTION = (
    BOLD
    + "Update the plugin versioning."
    + END
    + ITALICS
    + " This command should be run after finalizing any updates, defect fixes or "
    "new functionality, to update the versioning"
    + END
)
VIEW_DESCRIPTION = (
    BOLD
    + "View plugin docker container info"
    + END
    + ITALICS
    + "Provides an overview of the plugin"
    + END
)
