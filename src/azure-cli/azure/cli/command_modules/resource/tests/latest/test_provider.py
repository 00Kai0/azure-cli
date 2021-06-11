# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import ScenarioTest

class ProviderTests(ScenarioTest):

    def test_register(self):

        self.kwargs = {
            'namespace': "Microsoft.PolicyInsights"
        }

        self.cmd('provider unregister -n {namespace}')
        self.cmd('provider register -n {namespace} --consent-to-permissions')
        self.cmd('provider permission list -n {namespace}')
        self.cmd('provider unregister -n {namespace}')
        self.cmd('provider register -n {namespace}')
