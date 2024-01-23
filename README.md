# Ambiguous-AI-Assisted-Text-Codec
Ambiguous Artificial Intelligence Assisted File (De)Compression Technique


It's all in the title. Actually, the below code is only the compression part, which is simple. The code was written using GPT 3.5, and what it does is generate a Huffman Compression Table, but a modified one. How I modified it is, I had it take the least commonly occurring symbols, which have the longest code, erased that code, and assigned it to the same code as the most commonly occurring symbol, which has the shortest code. It lists the occurrence of the pairs in order as well, which should help a lot with decompression by removing tons of ambiguity. Obviously, it's still pretty ambiguous. How are we going to decompress a document which has had half of the data removed? That's where Artificial Intelligence comes to the rescue! Using a tool like Tensor Flow, we can now compress many text documents, and train a new AI by having it match both the compressed and uncompressed documents. With a large enough data set, it should be enough for a deployment of an AI with access to the API generated by the training data to decompress (actually to an extent, decrypt) the ambiguous document. In this way, we should have a proof of concept for a really efficient codec. 