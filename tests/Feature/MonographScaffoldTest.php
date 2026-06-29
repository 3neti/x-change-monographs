<?php

test('editorial canon exists', function () {
    expect(base_path('docs/editorial/editorial-canon-v2.md'))->toBeFile();
});

test('editorial manuscript specification exists', function () {
    expect(base_path('docs/editorial/editorial-manuscript-specification-v1.md'))->toBeFile();
});

test('volume 2 metadata exists', function () {
    expect(resource_path('monographs/volume-2/metadata/monograph.yaml'))->toBeFile();
});

test('volume 2 source manuscript exists', function () {
    expect(resource_path('monographs/volume-2/source/manuscript.md'))->toBeFile();
});

test('volume 2 editorial directory exists', function () {
    expect(resource_path('monographs/volume-2/editorial'))->toBeDirectory();
});

test('monograph status command runs successfully', function () {
    $this->artisan('monograph:status')
        ->expectsTable(
            ['Volume', 'Metadata', 'Source Manuscript', 'Editorial Directory'],
            [
                ['volume-1', 'yes', 'no', 'yes'],
                ['volume-2', 'yes', 'yes', 'yes'],
            ],
        )
        ->assertSuccessful();
});
