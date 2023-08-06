import click
from .modules.internals import project, authorization
from . import Stream, Dataset


@click.group()
def ffysh():
    pass


@ffysh.command()
def init():
    project.init_project()


@ffysh.command()
def login():
    authorization.login()


@ffysh.command()
@click.option('-d', '--dataset', help='Enter dataset ID which can be located in a dataset\'s URL.', required=True)
def download(dataset):
    """Downloads an entire dataset."""
    try:
        stream = Dataset(dataset_id=dataset).create_stream()
    except:
        click.echo("Dataset either is private or does not exist.")
        return
    stream.download(whole=True)


@ffysh.command()
@click.option('-d', '--dataset', help='Enter dataset ID which can be located in a dataset\'s URL.', required=True)
@click.option('-b', '--batch', type=int, help='Specifies the number of files to be downloaded. Starts off where specified stream ended or first file if stream is not specified', required=True)
@click.option('-c', '--chunk', type=int, help='The number of filed stored locally is equivalent to the chunk size plus the batch size.', required=True)
@click.option('-s', '--stream', help='Enter stream ID to continue chunking from a previous session.', required=False)
@click.option('-np', '--nopredownload', is_flag=True, help="Blocks downloading multiple files at once when iterating through the stream.")
@click.option('-r', '--reset', is_flag=True, help="Deletes all files (previous chunks) in saved stream directory")
@click.option('-ns', '--nosave', is_flag=True, help='Does not save stream to a directory. Assets can be found in the assets folder of the project directory.')
def load(dataset, batch, chunk, stream, nopredownload=False, reset=False, nosave=False):
    dataset_id = dataset
    batch_size = batch
    chunk_size = chunk
    stream_id = stream
    save = not nosave
    predownload = not nopredownload
    """Loads the next batch of a dataset."""
    if not isinstance(batch_size, int):
        raise AssertionError("Batch size must be an integer.")
    if batch_size <= 0:
        raise AssertionError("Batch size must be greater than 0.")
    if not isinstance(chunk_size, int):
        raise AssertionError("Chunk size must be an integer.")
    if chunk_size <= 0:
        raise AssertionError("Chunk size must be greater than 0.")

    try:
        dataset = Dataset(dataset_id=dataset_id)
    except:
        click.echo("Dataset either is private or does not exist.")
        return

    if stream is not None:
        try: 
            stream = Stream.load(saved_stream_id=stream_id)
        except:
            click.echo("Stream does not exist.")
            return
        if stream.dataset_id != dataset_id:
            click.echo(f"Stream belongs to incorrect dataset. Stream belongs to dataset {stream.dataset_id} while dataset {dataset_id} was specified.")
            return
        it = stream.create_iterator(start_index=stream._iterator_start_index, chunk_size=chunk_size, pre_download=predownload, batch_size=batch_size, save=save, reset=reset)
    else:
        stream = dataset.create_stream()
        click.echo(f"Created stream {stream.stream_id}. Use this stream ID to continue chunking from a previous session.")
        it = stream.create_iterator(start_index=0, chunk_size=chunk_size, pre_download=predownload, batch_size=batch_size, save=save, reset=reset)

    try:
        next(it)
    except StopIteration:
        click.echo("Stream already finished.")
        return
    
# @click.command()
# @click.option('-b', '--batch', default=64, help='# images per batch')
# @click.option('-B', '--buffer', default=16, help='# batches per buffer')
# @click.option('-d', '--dataset', help='relative path of zipped dataset (e.g. Dataset.zip)', required=True)
# def load(batch, buffer, dataset):
#     dataset_path = os.path.abspath(dataset)
#     load_pytorch(batch, buffer, dataset_path)


def main():
    ffysh()
