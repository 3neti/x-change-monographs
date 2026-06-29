<?php

namespace App\Console\Commands;

use Illuminate\Console\Attributes\Description;
use Illuminate\Console\Attributes\Signature;
use Illuminate\Console\Command;
use Illuminate\Support\Facades\File;
use Symfony\Component\Console\Command\Command as SymfonyCommand;

#[Signature('monograph:status')]
#[Description('List known monograph volumes and scaffold status')]
class MonographStatusCommand extends Command
{
    /**
     * Execute the console command.
     */
    public function handle(): int
    {
        $monographsPath = resource_path('monographs');

        if (! File::isDirectory($monographsPath)) {
            $this->error('No monograph directory found at resources/monographs.');

            return SymfonyCommand::FAILURE;
        }

        $volumeDirectories = collect(File::directories($monographsPath))
            ->sort()
            ->values();

        if ($volumeDirectories->isEmpty()) {
            $this->line('No monograph volumes found.');

            return SymfonyCommand::SUCCESS;
        }

        $rows = $volumeDirectories
            ->map(fn (string $directory): array => [
                basename($directory),
                File::exists($directory.'/metadata/monograph.yaml') ? 'yes' : 'no',
                File::exists($directory.'/source/manuscript.md') ? 'yes' : 'no',
                File::isDirectory($directory.'/editorial') ? 'yes' : 'no',
            ])
            ->all();

        $this->table(
            ['Volume', 'Metadata', 'Source Manuscript', 'Editorial Directory'],
            $rows,
        );

        return SymfonyCommand::SUCCESS;
    }
}
