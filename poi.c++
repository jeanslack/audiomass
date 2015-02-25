@try
 {
int read, write;
FILE *pcm = fopen([cafFilePath cStringUsingEncoding:1], "rb");  //source
fseek(pcm, 4*1024, SEEK_CUR);                                   //skip file header

mp3 = fopen([mp3FilePath cStringUsingEncoding:1], "wb");  //output
const int PCM_SIZE = 8192*3;
const int MP3_SIZE = 8192*3;
short int pcm_buffer[PCM_SIZE*2];
unsigned char mp3_buffer[MP3_SIZE];

lame_t lame = lame_init();
lame_set_in_samplerate(lame, 11025*2);
lame_set_VBR(lame, vbr_default);
lame_init_params(lame);

int nTotalRead=0;

do {
    read = fread(pcm_buffer, 2*sizeof(short int), PCM_SIZE, pcm);

    nTotalRead+=read*4;

    if (read == 0)
        write = lame_encode_flush(lame, mp3_buffer, MP3_SIZE);
    else
        write = lame_encode_buffer_interleaved(lame,pcm_buffer, read, mp3_buffer, MP3_SIZE);
    // write = lame_encode_buffer(lame, pcm_buffer,pcm_buffer, read, mp3_buffer, MP3_SIZE);

    fwrite(mp3_buffer, write, 1, mp3);
} while (read != 0);

lame_close(lame);
fclose(mp3);
fclose(pcm);
}
@catch (NSException *exception)
{
    NSLog(@"%@",[exception description]);
} 
