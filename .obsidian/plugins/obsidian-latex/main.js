'use strict';

const obsidian = require('obsidian');

const DEFAULT_SETTINGS = {
    preamblePath: "preamble.sty",
};

class JaxPlugin extends obsidian.Plugin {
    constructor(app, manifest) {
        super(app, manifest);
        this.settings = Object.assign({}, DEFAULT_SETTINGS);
    }

    async loadPreamble() {
        const preamble = await this.app.vault.adapter.read(this.settings.preamblePath);
        if (MathJax.tex2chtml == undefined) {
            MathJax.startup.ready = () => {
                MathJax.startup.defaultReady();
                MathJax.tex2chtml(preamble);
            };
        } else {
            MathJax.tex2chtml(preamble);
        }
    }

    async loadSettings() {
        this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
    }

    async saveSettings() {
        await this.saveData(this.settings);
    }

    async onload() {
        await this.loadSettings();
        this.addSettingTab(new JaxPluginSettingTab(this.app, this));

        // Load MathJax so that we can modify it
        // Otherwise, it would not be loaded when this plugin is loaded
        await obsidian.loadMathJax();
        if (typeof MathJax === "undefined" || !MathJax) {
            console.warn("MathJax was not defined despite loading it.");
            return;
        }
        await this.loadPreamble();
    }

    onunload() {
        // TODO: Is it possible to remove our definitions?
        console.log('Unloading Extended MathJax');
    }
}

class JaxPluginSettingTab extends obsidian.PluginSettingTab {
    constructor(app, plugin) {
        super(app, plugin);
        this.plugin = plugin;
    }

    display() {
        const { containerEl } = this;
        containerEl.empty();

        new obsidian.Setting(containerEl)
            .setName('Preamble path')
            .setDesc('Path to global preamble. (Requires reload!)')
            .addText((text) =>
                text
                    .setValue(this.plugin.settings.preamblePath)
                    .onChange(async (value) => {
                        this.plugin.settings.preamblePath = value;
                        await this.plugin.saveSettings();
                    })
            );
    }
}

module.exports = JaxPlugin;