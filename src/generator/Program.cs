using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;

namespace HashGenerator
{
    /* --------------------------------------------------------------------- */
    ///
    /// Program
    ///
    /// <summary>
    /// Represents the main program.
    /// </summary>
    ///
    /* --------------------------------------------------------------------- */
    class Program
    {
        /* ----------------------------------------------------------------- */
        ///
        /// Engines
        ///
        /// <summary>
        /// Gets the Hash algorithm engines.
        /// </summary>
        ///
        /* ----------------------------------------------------------------- */
        static readonly Dictionary<string, HashAlgorithm> Engines = new()
        {
            { "md5",    new MD5CryptoServiceProvider()    },
            { "sha1",   new SHA1CryptoServiceProvider()   },
            { "sha256", new SHA256CryptoServiceProvider() },
        };

        /* ----------------------------------------------------------------- */
        ///
        /// Invoke
        ///
        /// <summary>
        /// Calculates the hash values and shows the results.
        /// </summary>
        ///
        /// <param name="src">Source string.</param>
        /// <param name="json">Output format is json or not.</param>
        ///
        /* ----------------------------------------------------------------- */
        static void Invoke(string src, bool json)
        {
            if (!json) Console.WriteLine(src);

            foreach (var e in Engines)
            {
                var dest = e.Value.ComputeHash(Encoding.UTF8.GetBytes(src));
                var hex  = string.Join("", dest.Select(b => $"{b:x2}"));
                var b64  = Convert.ToBase64String(dest);

                if (json) Console.WriteLine($"{{ 'src': '{src}', 'kind': '{e.Key}', 'hex': '{hex}', 'base64': '{b64}' }}");
                else
                {
                    Console.WriteLine($"{e.Key,-8} (hex): {hex}");
                    Console.WriteLine($"{e.Key,-8} (b64): {b64}");
                }
            }

            if (!json) Console.WriteLine();
        }

        /* ----------------------------------------------------------------- */
        ///
        /// Main
        ///
        /// <summary>
        /// Represents the main function.
        /// </summary>
        ///
        /* ----------------------------------------------------------------- */
        static void Main(string[] args)
        {
            var json = args.Any() && args.First() == "json";
            foreach (var src in new[]
            {
                "Hello",
                "日本語のテスト",
                "0123456789",
            }) Invoke(src, json);
        }
    }
}
