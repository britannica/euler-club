<!-- EULER 22 in XSLT -->
<!-- Can be tested @http://fiddle.frameless.io/ (choose Saxon-CE) -->
<!-- ~30 seconds -->

<!-- The list of names needs to be converted into an XML file with this format: -->

<!--

<names>
    <name>MARY</name>
    <name>PATRICIA</name>
    <name>LINDA</name>
    <name>BARBARA</name>
    <name>ELIZABETH</name>
    <name>JENNIFER</name>
    <name>MARIA</name>
    <name>SUSAN</name>
    .....
</names>    

-->


<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0">

<xsl:template match="names">

    <!-- sort the list, the sorted list is copied into the $sortedList variable -->
    
    <xsl:variable name="sortedList">
        <xsl:for-each select="name">
            <xsl:sort select="." />
            <xsl:copy-of select="." />
        </xsl:for-each>
    </xsl:variable>
    
    <!-- each <name> node of the sorted list is processed, the template will create a -->
    <!-- <elt></elt> node for each name, the list of <elt></elt> is saved in the -->
    <!-- $individualSums variable -->
    
    <xsl:variable name="individualSums">

        <xsl:for-each select="$sortedList/name">    
    
            <!-- create a list of <elt></elt> for each name. Each <elt> contains the value of each letter -->
            <!-- of the name ( . - 64 = ASCII code of the letter - ASCII code of '@' (just before 'A')) -->

            <xsl:variable name="v" > 
                <xsl:for-each select="string-to-codepoints(.)">
                    <xsl:element name="elt"><xsl:value-of select="(. - 64)"/></xsl:element>
                </xsl:for-each>
            </xsl:variable>
            
            <!-- once the list is created, the template returns just an <elt></elt> -->
            <!-- which contains the sum of the value of each letter * position()  -->
            <!-- position() is the index of the loop (starting at 1) -->
            
            <xsl:element name="elt">
                 <xsl:value-of select="sum($v/elt) * position()"/>
          </xsl:element>

        </xsl:for-each>

    </xsl:variable>
    
    <!-- the xsl return the sum of the content of each <elt></elt> node -->
    
    <xsl:value-of select="sum($individualSums/elt)" />
 
</xsl:template>


</xsl:stylesheet>

<!-- output:
 
871198282

-->


